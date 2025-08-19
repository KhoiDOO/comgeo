import unittest
from comgeo.core.mesh.hybrid import HybridMesh
from comgeo.core.mesh.primitives.face import Face
from comgeo.core.mesh.primitives.quad_face import QuadFace
from comgeo.core.mesh.primitives.triangle_face import TriangleFace
from comgeo.core.vertex import Vertex2D, Vertex3D

class TestHybridMesh(unittest.TestCase):
	def setUp(self):
		self.vertices2d = [Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0), Vertex2D(1.0, 1.0), Vertex2D(0.0, 1.0)]
		self.vertices3d = [Vertex3D(0.0, 0.0, 0.0), Vertex3D(1.0, 0.0, 0.0), Vertex3D(1.0, 1.0, 0.0), Vertex3D(0.0, 1.0, 0.0)]
		self.faces = [[0, 1, 2, 3], [1, 2, 3, 0]]

	def test_init_2d_default_face(self):
		mesh = HybridMesh(self.vertices2d, self.faces, dim=2)
		self.assertEqual(len(mesh._faces), 2)
		self.assertTrue(all(isinstance(f, Face) for f in mesh._faces))

	def test_init_2d_quad_face(self):
		mesh = HybridMesh(self.vertices2d, self.faces, dim=2, face_type=QuadFace)
		self.assertTrue(all(isinstance(f, QuadFace) for f in mesh._faces))

	def test_init_3d_triangle_face(self):
		faces3d = [[0, 1, 2], [1, 2, 3]]
		mesh = HybridMesh(self.vertices3d, faces3d, dim=3, face_type=TriangleFace)
		self.assertTrue(all(isinstance(f, TriangleFace) for f in mesh._faces))

	def test_invalid_dim(self):
		with self.assertRaises(ValueError):
			HybridMesh(self.vertices2d, self.faces, dim=4)

	def test_invalid_vertex_type(self):
		with self.assertRaises(TypeError):
			HybridMesh([Vertex3D(0.0,0.0,0.0)], self.faces, dim=2)

	def test_from_file_path_not_implemented(self):
		# This test assumes load_mesh is not implemented or file does not exist
		with self.assertRaises(Exception):
			HybridMesh.from_file_path('nonexistent.obj', dim=2)

if __name__ == "__main__":
	unittest.main()