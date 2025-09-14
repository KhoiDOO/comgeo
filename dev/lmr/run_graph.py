import open3d as o3d
import numpy as np
import os
from collections import defaultdict

def process_mesh(mesh_path, output_dir, filename):
    """
    Reads a mesh, constructs its adjacency matrix, and reconstructs faces.
    """
    try:
        mesh = o3d.io.read_triangle_mesh(mesh_path)
    except Exception as e:
        print(f"Error reading {mesh_path}: {e}")
        return

    if not mesh.has_vertices() or not mesh.has_triangles():
        print(f"Skipping {mesh_path}: No vertices or triangles found.")
        return

    vertices = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.triangles)
    num_vertices = len(vertices)

    # --- 1. Build Edge Map and Adjacency Matrix ---
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    edge_face_count = defaultdict(int)

    for face in faces:
        for i in range(3):
            u, v = face[i], face[(i + 1) % 3]
            # Ensure u < v to have a consistent key for each edge
            edge = tuple(sorted((u, v)))
            edge_face_count[edge] += 1

    for edge, count in edge_face_count.items():
        u, v = edge
        if count >= 2:  # Shared by two or more faces
            adj_matrix[u, v] = 1
            adj_matrix[v, u] = 1
        elif count == 1:  # Boundary edge
            # As per rule: "only the value of lower triangle matrix is one"
            # We already sorted u,v so u is always smaller than v.
            # The prompt is slightly ambiguous, I'll set A[v,u] = 1 to be in lower triangle
            adj_matrix[v, u] = 1


    # --- 2. Reconstruct edge_face_count from adj_matrix ---
    reconstructed_edge_face_count = defaultdict(int)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            is_internal = adj_matrix[i, j] == 1 and adj_matrix[j, i] == 1
            # Assuming i < j, boundary edge was set as adj_matrix[j, i] = 1
            is_boundary = adj_matrix[j, i] == 1 and adj_matrix[i, j] == 0

            if is_internal:
                reconstructed_edge_face_count[(i, j)] = 2
            elif is_boundary:
                reconstructed_edge_face_count[(i, j)] = 1

    # --- 3. Reconstruct Mesh Faces from reconstructed_edge_face_count ---
    reconstructed_faces = []
    
    # Iterate through all possible triplets of vertices to find faces
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            # Check for an edge between i and j
            if (i, j) in reconstructed_edge_face_count:
                for k in range(j + 1, num_vertices):
                    # Check for edges between (i, k) and (j, k)
                    if (i, k) in reconstructed_edge_face_count and \
                       (j, k) in reconstructed_edge_face_count:
                        reconstructed_faces.append([i, j, k])

    # --- 4. Export Reconstructed Mesh ---
    recon_mesh = o3d.geometry.TriangleMesh()
    recon_mesh.vertices = o3d.utility.Vector3dVector(vertices)
    recon_mesh.triangles = o3d.utility.Vector3iVector(np.array(reconstructed_faces))
    
    output_path = os.path.join(output_dir, filename)
    o3d.io.write_triangle_mesh(output_path, recon_mesh)

    print(f"Processed {os.path.basename(mesh_path)}:")
    print(f"  - Vertices: {num_vertices}")
    print(f"  - Original faces: {len(faces)}")
    print(f"  - Adjacency matrix shape: {adj_matrix.shape}")
    print(f"  - Reconstructed edge_face_count: {len(reconstructed_edge_face_count)}")
    print(f"  - Reconstructed faces: {len(reconstructed_faces)}")
    print(f"  - Saved reconstructed mesh to {output_path}")
    print("-" * 20)


def main():
    """
    Main function to process all .obj files in the specified directory.
    """
    mesh_dir = os.path.join(os.path.dirname(__file__), 'm500_ori')
    recon_mesh_dir = os.path.join(os.path.dirname(__file__), 'm500_recon_adj')
    os.makedirs(recon_mesh_dir, exist_ok=True)
    obj_files = [f for f in os.listdir(mesh_dir) if f.endswith('.obj')]

    for obj_file in obj_files:
        mesh_path = os.path.join(mesh_dir, obj_file)
        process_mesh(mesh_path, recon_mesh_dir, obj_file)

if __name__ == "__main__":
    main()
