import matplotlib.pyplot as plt
from comgeo.core.vertex import Vertex2D, Vertex3D
from comgeo.core.mesh.triangle_mesh import TriangleMesh2D
from comgeo.core.mesh.primitives.face import Face
import os

def plot_mesh_and_points(mesh: TriangleMesh2D, points: list[Vertex2D | Vertex3D], pdf_path: str):
	# Plot mesh edges in blue
	for face in mesh.faces:
		face: Face
		coords = [mesh.vertices[i] for i in face.vertex_ids]
		xs = [v.x for v in coords]
		ys = [v.y for v in coords]
		xs.append(xs[0])
		ys.append(ys[0])
		plt.plot(xs, ys, color='blue', linewidth=1)
	# Plot point cloud in red
	px = [p.x for p in points]
	py = [p.y for p in points]
	plt.scatter(px, py, color='red', s=1, alpha=0.6)
	plt.gca().set_aspect('equal')
	plt.savefig(pdf_path)
	plt.close()

if __name__ == "__main__":
	base_dir = os.path.dirname(os.path.abspath(__file__))
	mesh_path = os.path.normpath(os.path.join(base_dir, '..', '..', 'sample', '2dmesh', 'o.obj'))
	pdf_path = os.path.join(base_dir, "2dpc.pdf")
	mesh = TriangleMesh2D.from_file_path(mesh_path)
	points: list[Vertex2D | Vertex3D] = mesh.point_cloud_sampling(3000)
	print(f"Sampled {len(points)} points from the mesh.")
	plot_mesh_and_points(mesh, points, pdf_path)

	