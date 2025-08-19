
import unittest
import numpy as np
from comgeo.core.mesh.base import Mesh
from comgeo.core.vertex import Vertex2D

class DummyVertex:
	pass

class TestMesh(unittest.TestCase):
	def setUp(self):
		self.verts2d = [Vertex2D(0.0,0.0), Vertex2D(1.0,0.0), Vertex2D(0.0,1.0)]
		self.faces = [[0, 1, 2]]
		self.mesh = Mesh(self.verts2d, self.faces)

	def test_init(self):
		self.assertEqual(self.mesh.faces, self.faces)
		self.assertIsInstance(self.mesh.face_adjacency_matrix, np.ndarray)
		self.assertEqual(self.mesh.face_adjacency_matrix.shape, (1, 1))
		self.assertFalse(self.mesh.has_face_adjacency_matrix)

	def test_faces_setter(self):
		new_faces = [[0, 2, 1]]
		self.mesh.faces = new_faces
		self.assertEqual(self.mesh.faces, new_faces)
		with self.assertRaises(ValueError):
			self.mesh.faces = []

	def test_invalid_vertex_type(self):
		verts = [DummyVertex()]
		faces = [[0]]
		with self.assertRaises(ValueError):
			Mesh(verts, faces)

	def test_face_adjacency_matrix_properties(self):
		self.assertIsInstance(self.mesh.face_adjacency_matrix, np.ndarray)
		self.assertFalse(self.mesh.has_face_adjacency_matrix)

	def test_connected_components_properties(self):
		self.assertIsInstance(self.mesh.connected_components, list)
		self.assertFalse(self.mesh.has_connected_components)

	def test_vertex2face_properties(self):
		self.assertIsInstance(self.mesh.vertex2face, list)
		self.assertFalse(self.mesh.has_vertex2face)

	def test_vertex2cc_properties(self):
		self.assertIsInstance(self.mesh.vertex2cc, list)
		self.assertFalse(self.mesh.has_vertex2cc)

	def test_vertex_adjacency_matrix_properties(self):
		self.assertIsInstance(self.mesh.vertex_adjacency_matrix, np.ndarray)
		self.assertFalse(self.mesh.has_vertex_adjacency_matrix)

	def test_vertex_adjacency_list_properties(self):
		# Accept dict or list for compatibility with implementation
		self.assertTrue(isinstance(self.mesh.vertex_adjacency_list, (list, dict)))
		self.assertFalse(self.mesh.has_vertex_adjacency_list)

	def test_not_self_implemented_methods(self):
		# All should raise NotImplementedError
		with self.assertRaises(NotImplementedError):
			Mesh.from_file_path('dummy.obj')
		with self.assertRaises(NotImplementedError):
			self.mesh.export_to_file_path('dummy.obj')
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_face_adjacency_matrix()
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_connected_components()
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_vertex2face()
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_vertex2cc()
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_vertex_adjacency_matrix()
		with self.assertRaises(NotImplementedError):
			self.mesh.construct_vertex_adjacency_list()
		with self.assertRaises(NotImplementedError):
			self.mesh.point_cloud_sampling(10)
		with self.assertRaises(NotImplementedError):
			self.mesh.visualize()

if __name__ == "__main__":
	unittest.main()
