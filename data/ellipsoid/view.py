import bpy
import os
import math
import mathutils # Import the mathutils module
import sys       # Import the sys module to access command-line arguments

main_data_dir = os.path.normpath(os.path.join(os.getcwd(), '..', '..'))
sys.path.append(main_data_dir)

def import_obj(filepath):
    
    # Get object name
    object_name = os.path.basename(filepath).split('.')[0]
    
    # Store the current objects in the scene
    existing_objects = set(bpy.context.scene.objects)

    # Import the .obj file
    bpy.ops.wm.obj_import(
        filepath=filepath,
        global_scale=1,
        forward_axis='X',
        up_axis='Z',
        validate_meshes=True,
        filter_glob='*.obj'
    )

    # Determine the newly imported objects
    new_objects = set(bpy.context.scene.objects) - existing_objects

    # Set the location and name for each new object
    for obj in new_objects:
        obj.name = object_name
        if obj.data:
            obj.data.name = object_name
            
    # print(f'[INFO] Importing {object_name} from {filepath}')
    
    return object_name

# --- Configuration ---
# This should match the OUTPUT_DIRECTORY from your ellipsoid generation script
INPUT_DIRECTORY = os.path.normpath(os.path.join(os.getcwd(), 'ellipsoid_simple'))

# Default number of OBJ files to load if no argument is provided
DEFAULT_NUM_FILES_TO_LOAD = 25

# A factor to add padding between objects based on their size.
GRID_PADDING_FACTOR = 1.2

SAVE_BLEND_FILE = True # Set to True to save the .blend file
BLEND_FILE_NAME = "ellipsoid_grid.blend" # Name of the .blend file to save

# --- Helper Functions ---

def clear_scene():
    """Clears all objects from the current scene."""
    # Deselect all objects first
    bpy.ops.object.select_all(action='DESELECT')
    # Select all mesh objects, cameras, and lights
    for obj in bpy.data.objects:
        if obj.type in {'MESH', 'CAMERA', 'LIGHT'}:
            obj.select_set(True)
    # Delete selected objects
    bpy.ops.object.delete()
    # Ensure collections are also clean if necessary
    for collection in bpy.data.collections:
        if collection.users == 0:
            bpy.data.collections.remove(collection)
    # Clean up materials that are no longer used
    for material in bpy.data.materials:
        if material.users == 0:
            bpy.data.materials.remove(material)

def get_max_object_dimension(file_list, input_path):
    """
    Scans a list of OBJ files to find the maximum dimension among all objects.
    
    Args:
        file_list (list): A list of filenames to scan.
        input_path (str): The absolute path to the directory containing the files.
        
    Returns:
        float: The maximum dimension found across all objects.
    """
    max_dim = 0.0
    for filename in file_list:
        filepath = os.path.join(input_path, filename)
        
        # Import the OBJ file temporarily
        import_obj(filepath)
        imported_obj = bpy.context.selected_objects[0]
        
        # Find the largest dimension of the imported object
        dims = imported_obj.dimensions
        current_max = max(dims.x, dims.y, dims.z)
        if current_max > max_dim:
            max_dim = current_max
            
        # Delete the temporary object to keep the scene clean
        bpy.data.objects.remove(imported_obj, do_unlink=True)

    return max_dim


def setup_camera_and_light_for_grid(num_objects, grid_cols, grid_spacing):
    """Sets up a camera and light suitable for viewing the grid."""
    # Calculate approximate grid dimensions
    rows = math.ceil(num_objects / grid_cols)
    grid_width = (grid_cols - 1) * grid_spacing
    grid_height = (rows - 1) * grid_spacing

    # Adjust camera position based on grid size
    cam_x = grid_width / 2.0
    cam_y = -max(grid_width, grid_height) * 1.5 # Move camera back
    cam_z = max(grid_width, grid_height) * 0.8 # Move camera up

    # Add Camera
    bpy.ops.object.camera_add(location=(cam_x, cam_y, cam_z))
    camera = bpy.context.object
    bpy.context.scene.camera = camera
    # Point camera at the center of the grid
    look_at_target = (grid_width / 2.0, grid_height / 2.0, 0)
    # Use mathutils.Vector instead of bpy.Vector
    direction = (mathutils.Vector(look_at_target) - camera.location).normalized()
    # Rotation based on direction vector
    rot_quat = direction.to_track_quat('-Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()

    # Add Sun Light
    bpy.ops.object.light_add(type='SUN', location=(cam_x, cam_y / 2, cam_z * 1.5))
    light = bpy.context.object
    light.data.energy = 2.0 # Adjust light intensity
    # Point light towards the grid
    # Use mathutils.Vector instead of bpy.Vector
    light_direction = (mathutils.Vector(look_at_target) - light.location).normalized()
    light_rot_quat = light_direction.to_track_quat('-Z', 'Y')
    light.rotation_euler = light_rot_quat.to_euler()


# --- Main Script ---

def load_ellipsoids_into_grid(num_files_to_load_arg, obj_type="quad"):
    """
    Loads OBJ ellipsoids from a specified directory and arranges them in a grid.

    Args:
        num_files_to_load_arg (int): The number of OBJ files to load and display.
    """
    # Use the argument for NUM_FILES_TO_LOAD
    num_files_to_load = num_files_to_load_arg
    
    # Get the absolute path to the input directory
    input_path = bpy.path.abspath(INPUT_DIRECTORY)

    if not os.path.isdir(input_path):
        print(f"Error: Input directory not found: {input_path}")
        return

    # Get all OBJ files in the directory
    obj_files = sorted([f for f in os.listdir(input_path) if f.endswith(f'_{obj_type}.obj')])
    obj_files_to_load = obj_files[:num_files_to_load]

    if not obj_files_to_load:
        print(f"No OBJ files found to load from {input_path}")
        return

    # Clear the scene before we begin
    clear_scene()

    # First, determine the largest object dimension to set the grid spacing
    print("Scanning objects to determine optimal grid spacing...")
    max_dim = get_max_object_dimension(obj_files_to_load, input_path)
    grid_spacing = max_dim * GRID_PADDING_FACTOR
    
    print(f"Largest object dimension is {max_dim:.2f}. Calculated grid spacing is {grid_spacing:.2f}")

    # Now we can start the final placement
    grid_cols = math.ceil(math.sqrt(num_files_to_load)) # Recalculate GRID_COLS based on the argument
    setup_camera_and_light_for_grid(num_files_to_load, grid_cols, grid_spacing)

    print(f"Loading up to {num_files_to_load} ellipsoids from {input_path}...")

    loaded_count = 0
    for i, filename in enumerate(obj_files_to_load):
        filepath = os.path.join(input_path, filename)

        import_obj(filepath)
        imported_obj = bpy.context.selected_objects[0]
        
        if imported_obj:
            imported_obj.name = f"GridEllipsoid_{i:04d}"

            # Calculate grid position
            col = loaded_count % grid_cols
            row = loaded_count // grid_cols

            imported_obj.location = (
                col * grid_spacing,
                row * grid_spacing,
                0 # Keep Z at 0 for a flat grid
            )
            print(f"Loaded {filename} at ({imported_obj.location.x:.2f}, {imported_obj.location.y:.2f}, {imported_obj.location.z:.2f})")
            loaded_count += 1
        else:
            print(f"Warning: Could not import {filename}")

    print(f"Successfully loaded {loaded_count} ellipsoids into a grid.")

    # Save the .blend file
    if SAVE_BLEND_FILE:
        blend_filepath = f"{obj_type}_{BLEND_FILE_NAME}"
        bpy.ops.wm.save_as_mainfile(filepath=blend_filepath)
        print(f"Saved Blender file: {blend_filepath}")


# --- Run the script ---
if __name__ == "__main__":
    try:
        idx = sys.argv.index("--")
        args = sys.argv[idx+1:]
    except ValueError:
        args = [] 

    num_files = DEFAULT_NUM_FILES_TO_LOAD # Use default if no argument is given

    if args:
        try:
            num_files = int(args[0]) 
            if num_files <= 0:
                raise ValueError("Number of files must be positive.")
            print(f"Using NUM_FILES_TO_LOAD from argument: {num_files}")
        except (ValueError, IndexError):
            print(f"Invalid or missing argument for NUM_FILES_TO_LOAD. Using default: {DEFAULT_NUM_FILES_TO_LOAD}")
    else:
        print(f"No argument provided for NUM_FILES_TO_LOAD. Using default: {DEFAULT_NUM_FILES_TO_LOAD}")

    # load_ellipsoids_into_grid(num_files, obj_type="quad")
    load_ellipsoids_into_grid(num_files, obj_type="tria")

