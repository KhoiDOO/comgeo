import matplotlib.pyplot as plt
from comgeo.core.vertex import Vertex2D, Vertex3D
from comgeo.core.mesh.triangle_mesh import TriangleMesh2D
from comgeo.core.mesh.primitives.face import Face
from comgeo.functional.mesh.delaunay.dt import delaunay_triangulation_naive
import os

def plot_mesh_and_points(mesh: TriangleMesh2D, recon_mesh: TriangleMesh2D, pdf_path: str):
	fig, axes = plt.subplots(1, 2, figsize=(12, 6))
	# Plot original mesh and point cloud on the left
	ax1 = axes[0]
	for face in mesh.faces:
		face: Face
		coords = [mesh.vertices[i] for i in face.vertex_ids]
		xs = [v.x for v in coords]
		ys = [v.y for v in coords]
		xs.append(xs[0])
		ys.append(ys[0])
		ax1.plot(xs, ys, color='blue', linewidth=1)
	# Removed point cloud plotting
	ax1.set_title('Original Mesh & Point Cloud')
	ax1.set_aspect('equal')

	# Plot reconstructed mesh on the right
	ax2 = axes[1]
	for face in recon_mesh.faces:
		coords = [recon_mesh.vertices[i] for i in face.vertex_ids]
		xs = [v.x for v in coords]
		ys = [v.y for v in coords]
		xs.append(xs[0])
		ys.append(ys[0])
		ax2.plot(xs, ys, color='green', linewidth=1)
	ax2.set_title('Reconstructed Mesh from Point Cloud')
	ax2.set_aspect('equal')

	plt.tight_layout()
	plt.savefig(pdf_path)
	plt.close()

if __name__ == "__main__":
	base_dir = os.path.dirname(os.path.abspath(__file__))
	mesh_path = os.path.normpath(os.path.join(base_dir, '..', '..', 'sample', '2dmesh', 'o.obj'))
	pdf_path = os.path.join(base_dir, "2d_recon.pdf")
	mesh = TriangleMesh2D.from_file_path(mesh_path)
	recon_mesh = delaunay_triangulation_naive(mesh.vertices, verbose=True, progress_bar=False, refine=False)
	plot_mesh_and_points(mesh, recon_mesh, pdf_path)