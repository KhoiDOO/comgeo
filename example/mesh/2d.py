import matplotlib.pyplot as plt
from comgeo.core.mesh.triangle_mesh import TriangleMesh2D
from comgeo.core.mesh.primitives.face import Face
import os

def plot_mesh(mesh: TriangleMesh2D, filename: str):
	for face in mesh.faces:
		face: Face
		coords = [mesh.vertices[i] for i in face.vertex_ids]
		xs = [v.x for v in coords]
		ys = [v.y for v in coords]
		xs.append(xs[0])
		ys.append(ys[0])
		plt.plot(xs, ys, 'k-')
	plt.gca().set_aspect('equal')
	plt.savefig(filename)
	plt.close()

if __name__ == "__main__":
	base_dir = os.path.dirname(os.path.abspath(__file__))
	mesh_path = os.path.join(base_dir, "2d.obj")
	pdf_path = os.path.join(base_dir, "2d.pdf")
	mesh = TriangleMesh2D.from_file_path(mesh_path)
	plot_mesh(mesh, pdf_path)
