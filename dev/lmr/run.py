from scipy.spatial import Delaunay
from collections import Counter

import os
import open3d as o3d
import numpy as np

def get_obj_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.obj')]

def sample_points_in_tetrahedron(tetra_vertices, num_points):
    v0, v1, v2, v3 = tetra_vertices

    # A more stable method for barycentric coordinates
    r1 = np.random.rand(num_points)
    r2 = np.random.rand(num_points)
    r3 = np.random.rand(num_points)
    r4 = 1 - r1 - r2 - r3

    # Calculate points using the barycentric coordinates
    points = r1[:, np.newaxis] * v0 + r2[:, np.newaxis] * v1 + r3[:, np.newaxis] * v2 + r4[:, np.newaxis] * v3

    return points

def mesh_from_tetras(vertices: np.ndarray, tetrahedrons: np.ndarray) -> o3d.geometry.TriangleMesh:
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    triangles = tetrahedrons[:, [0, 1, 2, 0, 2, 3, 0, 1, 3, 1, 2, 3]]
    triangles = triangles.reshape(-1, 3)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    return mesh

def main():
    originals_folder = os.path.join(os.path.dirname(__file__), 'originals')
    recon_delaunay_folder = os.path.join(os.path.dirname(__file__), 'recon_delaunay')
    recon_voting_folder = os.path.join(os.path.dirname(__file__), 'recon_voting')
    os.makedirs(recon_delaunay_folder, exist_ok=True)
    os.makedirs(recon_voting_folder, exist_ok=True)

    obj_files = get_obj_files(originals_folder)
    for obj_path in obj_files:
        
        mesh = o3d.io.read_triangle_mesh(obj_path)
        mesh.compute_vertex_normals()
        vertices = np.asarray(mesh.vertices)

        print(f"Processing {obj_path} with {len(vertices)} vertices.")
        
        mesh_t = o3d.t.geometry.TriangleMesh.from_legacy(mesh)
        scene = o3d.t.geometry.RaycastingScene()
        scene.add_triangles(mesh_t)

        print(f'Successfully created raycasting scene for {obj_path}')

        delaunay_tri = Delaunay(vertices)
        tetrahedrons = delaunay_tri.simplices

        print(f"Extracted {len(tetrahedrons)} tetrahedrons.")

        # triangles = tetrahedrons[:, [0, 1, 2, 0, 2, 3, 0, 1, 3, 1, 2, 3]]
        # print(triangles[:5])
        print(f'Creating mesh from tetrahedrons...')
        recon_mesh_tetra = mesh_from_tetras(vertices, tetrahedrons)
        o3d.io.write_triangle_mesh(os.path.join(recon_delaunay_folder, f'delaunay_{os.path.basename(obj_path)}'), recon_mesh_tetra)

        print("\nPerforming multi-label voting for each tetrahedron...")

        initial_tetra_labels = np.empty(len(tetrahedrons), dtype=object)
        num_sample_points = 101

        for i, tetra_indices in enumerate(tetrahedrons):
            tetra_verts = vertices[tetra_indices]
            points_to_test = sample_points_in_tetrahedron(tetra_verts, num_sample_points)
            signed_distances = scene.compute_signed_distance(points_to_test.astype(np.float32)).numpy()
            votes_inside = np.sum(signed_distances < 0)
            label = "inside" if votes_inside > (num_sample_points / 2) else "outside"
            initial_tetra_labels[i] = label

            # Progress indicator
            # if (i + 1) % 2000 == 0:
            #     print(f"  Voted on {i + 1}/{len(tetrahedrons)} tetrahedrons...")
        
        refined_tetra_labels = np.copy(initial_tetra_labels)
    
        # The paper suggests this optimization helps create manifold meshes.
        # We iterate and adjust labels based on what the neighbors' labels are.
        for i in range(len(tetrahedrons)):
            neighbor_indices = delaunay_tri.neighbors[i]
            valid_neighbors = neighbor_indices[neighbor_indices != -1]
            if len(valid_neighbors) == 0:
                continue
            neighbor_labels = initial_tetra_labels[valid_neighbors]
            label_counts = Counter(neighbor_labels)
            majority_label = label_counts.most_common(1)[0][0]
            
            refined_tetra_labels[i] = majority_label
        
        inside_count = np.sum(refined_tetra_labels == "inside")
        outside_count = len(refined_tetra_labels) - inside_count
        print(f"Result: {inside_count} tetrahedrons labeled 'inside', {outside_count} labeled 'outside'.")

        print("\nExtracting surface by finding boundaries between refined labels...")
        face_map = {}
        for i, tetra in enumerate(tetrahedrons):
            label = refined_tetra_labels[i] # Use the refined labels
            faces = [
                (tetra[0], tetra[1], tetra[2]),
                (tetra[0], tetra[1], tetra[3]),
                (tetra[0], tetra[2], tetra[3]),
                (tetra[1], tetra[2], tetra[3]),
            ]
            for face in faces:
                face_key = tuple(sorted(face))
                if face_key not in face_map:
                    face_map[face_key] = []
                face_map[face_key].append(label)

        surface_faces = []
        for face_key, labels in face_map.items():
            if len(labels) == 2 and labels[0] != labels[1]:
                surface_faces.append(list(face_key))

        print(f"Extracted {len(surface_faces)} faces for the new surface mesh.")

        # --- 7. Create and Visualize Final Mesh ---
        if not surface_faces:
            print("Could not find any surface faces. The resulting mesh is empty.")
        else:
            reconstructed_mesh = o3d.geometry.TriangleMesh()
            reconstructed_mesh.vertices = o3d.utility.Vector3dVector(vertices)
            reconstructed_mesh.triangles = o3d.utility.Vector3iVector(surface_faces)

            o3d.io.write_triangle_mesh(os.path.join(recon_voting_folder, f'lmr_{os.path.basename(obj_path)}'), reconstructed_mesh)

if __name__ == "__main__":
    main()
