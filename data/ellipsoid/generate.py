import bpy
import random
import os
import math
import sys
import shutil

def export_obj(filepath, export_triangle=True):

    bpy.ops.wm.obj_export(
        filepath=filepath,
        check_existing=True,
        filter_blender=False,
        filter_backup=False,
        filter_image=False,
        filter_movie=False,
        filter_python=False,
        filter_font=False,
        filter_sound=False,
        filter_text=False,
        filter_archive=False,
        filter_btx=False,
        filter_collada=False,
        filter_alembic=False,
        filter_usd=False,
        filter_obj=False,
        filter_volume=False,
        filter_folder=True,
        filter_blenlib=False,
        filemode=8,
        display_type='DEFAULT',
        sort_method='DEFAULT',
        export_animation=False,
        start_frame=-2147483648,
        end_frame=2147483647,
        forward_axis='X',
        up_axis='Z',
        global_scale=1.0,
        apply_modifiers=False,
        export_eval_mode='DAG_EVAL_VIEWPORT',
        export_selected_objects=True,
        export_uv=False,
        export_normals=False,
        export_colors=False,
        export_materials=False,
        export_pbr_extensions=False,
        path_mode='AUTO',
        export_triangulated_mesh=export_triangle,
        export_curves_as_nurbs=False,
        export_object_groups=False,
        export_material_groups=False,
        export_vertex_groups=False,
        export_smooth_groups=False,
        smooth_group_bitflags=False,
        filter_glob='*.obj;*.mtl'
    )

# --- Configuration ---
DEFAULT_NUM_ELLIPSOIDS = 50  # Number of ellipsoids to generate
OUTPUT_DIRECTORY = os.path.normpath(
    os.path.join(os.getcwd(), 'ellipsoid_simple')  # Relative path to output directory
)  # Output directory relative to the .blend file
MIN_SEMI_AXIS = 0.2 # Adjusted minimum to allow for smaller ellipsoids
MAX_SEMI_AXIS = 1 # Max semi-axis to fit within a unit cube (extent from origin is 0.5)

# --- Helper Functions ---

def clear_scene():
    """Clears all objects from the current scene."""
    # Deselect all objects first
    bpy.ops.object.select_all(action='DESELECT')
    # Select all mesh objects
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
    # Delete selected objects
    bpy.ops.object.delete()
    # Ensure collections are also clean if necessary (optional, but good practice)
    for collection in bpy.data.collections:
        if collection.users == 0:
            bpy.data.collections.remove(collection)
    # Clean up materials that are no longer used
    for material in bpy.data.materials:
        if material.users == 0:
            bpy.data.materials.remove(material)

# --- Main Script ---

def generate_ellipsoid_dataset(num_ellipsoids_arg):
    """
    Generates a dataset of ellipsoids with varying properties and exports them as OBJ files.

    Args:
        num_ellipsoids_arg (int): The number of ellipsoids to generate.
    """
    num_ellipsoids = num_ellipsoids_arg

    output_path = bpy.path.abspath(OUTPUT_DIRECTORY)
    if os.path.exists(output_path):
        # If the directory exists, clear it
        print(f"Output directory {output_path} already exists. Clearing it...")
        shutil.rmtree(output_path)
    os.makedirs(output_path, exist_ok=True)

    # Clear previous objects from the scene
    clear_scene()

    print(f"Generating {num_ellipsoids} ellipsoids and exporting to OBJ...")

    for i in range(num_ellipsoids):
        # Generate random semi-axes
        # Ensure semi-minor and semi-major are distinct by picking three different values
        # and then assigning them randomly to x, y, z scales.
        axis_values = [random.uniform(MIN_SEMI_AXIS, MAX_SEMI_AXIS) for _ in range(3)]
        random.shuffle(axis_values) # Shuffle to randomly assign major/minor axes

        scale_x = axis_values[0]
        scale_y = axis_values[1]
        scale_z = axis_values[2]

        # Add a cube instead of a UV sphere to ensure a quad-based mesh
        bpy.ops.mesh.primitive_cube_add(
            size=1.0, # size 2.0 to fit within (-1, 1), size 1.0 would fit within (-0.5, 0.5)
            enter_editmode=False,
            align='WORLD',
            location=(0, 0, 0) # Always create at origin
        )
        ellipsoid = bpy.context.object
        ellipsoid.name = f"Ellipsoid_{i:05d}" # Give each ellipsoid a unique name

        # Add a Subdivision Surface modifier
        subd_modifier = ellipsoid.modifiers.new(name="Subdivision", type='SUBSURF')
        subd_modifier.levels = 2 # Increase for a smoother sphere-like mesh

        # Apply the modifier to convert the subdivided cube into a quad-based sphere
        bpy.context.view_layer.objects.active = ellipsoid
        bpy.ops.object.modifier_apply(modifier="Subdivision")

        # Apply scaling to make it an ellipsoid
        ellipsoid.scale = (scale_x, scale_y, scale_z)

        # Set position to the origin to keep it within the unit cube
        ellipsoid.location = (0, 0, 0)

        # Randomize rotation
        ellipsoid.rotation_euler = (
            random.uniform(0, 2 * math.pi),
            random.uniform(0, 2 * math.pi),
            random.uniform(0, 2 * math.pi)
        )

        # Apply transformations (important for correct export)
        # This converts the scale and rotation into actual mesh data
        bpy.ops.object.select_all(action='DESELECT')
        ellipsoid.select_set(True)
        bpy.context.view_layer.objects.active = ellipsoid
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        # Update the scene to apply transformations before export
        bpy.context.view_layer.update()

        # Export the current ellipsoid to an OBJ file
        obj_filename = f"ellipsoid_{i:05d}.obj"
        obj_filepath = os.path.join(output_path, obj_filename)

        export_obj(obj_filepath, export_triangle=True)

        # Deselect the ellipsoid after export
        ellipsoid.select_set(False)

        # Delete the ellipsoid from the scene to prepare for the next one
        bpy.data.objects.remove(ellipsoid, do_unlink=True)

    print("Dataset generation and OBJ export complete!")

# --- Run the script ---
if __name__ == "__main__":
    # Check for command-line arguments
    # sys.argv will contain: ['blender', '--background', '--python', 'your_script.py', '--', 'arg1', 'arg2', ...]
    # We are looking for arguments after '--'
    try:
        idx = sys.argv.index("--")
        args = sys.argv[idx+1:]
    except ValueError:
        args = [] # No custom arguments provided

    num_ellipsoids_to_generate = DEFAULT_NUM_ELLIPSOIDS # Use default if no argument is given

    if args:
        try:
            num_ellipsoids_to_generate = int(args[0]) # Expecting the first argument to be the number of ellipsoids
            if num_ellipsoids_to_generate <= 0:
                raise ValueError("Number of ellipsoids must be positive.")
            print(f"Using NUM_ELLIPSOIDS from argument: {num_ellipsoids_to_generate}")
        except (ValueError, IndexError):
            print(f"Invalid or missing argument for NUM_ELLIPSOIDS. Using default: {DEFAULT_NUM_ELLIPSOIDS}")
    else:
        print(f"No argument provided for NUM_ELLIPSOIDS. Using default: {DEFAULT_NUM_ELLIPSOIDS}")

    generate_ellipsoid_dataset(num_ellipsoids_to_generate)