import unittest
from comgeo.core.mesh.primitives.face import Face
from comgeo.core.vertex import Vertex2D, Vertex3D, Vertex

class TestFace(unittest.TestCase):
	def setUp(self):
		self.vertex_ids = [0, 1, 2]
		self.face = Face(self.vertex_ids, id=5, visited=True, max_num_vertices=4)
		self.vertices2d = [Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0), Vertex2D(0.0, 1.0)]
		self.vertices3d = [Vertex3D(0.0, 0.0, 0.0), Vertex3D(1.0, 0.0, 0.0), Vertex3D(0.0, 1.0, 0.0)]

		self.face_convex_1 = Face([0, 1, 2, 3, 4, 5], id=6, visited=True, max_num_vertices=6)
		self.vertices2d_convex = [Vertex2D(0.0, -2.0), Vertex2D(1.0, 0.0), Vertex2D(0.0, 1.0), Vertex2D(-0.5, 0.5), Vertex2D(-0.6, 0.0), Vertex2D(-0.5, -1.0)]
		self.face_convex_2 = Face([5, 4, 3, 2, 1, 0], id=7, visited=True, max_num_vertices=6)
		self.vertices2d_non_convex = [Vertex2D(0.0, -1.0), Vertex2D(1.0, 0.0), Vertex2D(0.0, 1.0), Vertex2D(-0.5, 0.5), Vertex2D(-0.5, 0.0), Vertex2D(1.0, 1.0)]
		self.face_non_convex = Face([0, 1, 2, 3, 4, 5], id=8, visited=True, max_num_vertices=6)

	def test_init_and_properties(self):
		self.assertEqual(self.face.id, 5)
		self.assertTrue(self.face.visited)
		self.assertEqual(self.face.vertex_ids, self.vertex_ids)
		self.assertIsNone(self.face._center)
		self.assertIsNone(self.face._area)
		self.assertEqual(self.face._max_num_vertices, 4)

	def test_id_setter(self):
		self.face.id = 10
		self.assertEqual(self.face.id, 10)

	def test_visited_setter(self):
		self.face.visited = False
		self.assertFalse(self.face.visited)

	def test_vertex_ids_setter(self):
		new_ids = [1, 2, 0]
		self.face.vertex_ids = new_ids
		self.assertEqual(self.face.vertex_ids, new_ids)

	def test_vertex_ids_setter_exceeds_max(self):
		with self.assertRaises(AssertionError):
			self.face.vertex_ids = [0, 1, 2, 3, 4]

	def test_repr_and_str(self):
		expected = f"Face(id=5, visited=True, \nvertex_ids={self.vertex_ids})"
		self.assertEqual(repr(self.face), expected)
		self.assertEqual(str(self.face), expected)

	def test_get_set_item(self):
		self.assertEqual(self.face[0], 0)
		self.face[0] = 9
		self.assertEqual(self.face[0], 9)

	def test_equality(self):
		other = Face([0, 1, 2], id=5, visited=True, max_num_vertices=4)
		self.assertTrue(self.face == other)
		other2 = Face([0, 1, 3], id=5, visited=True, max_num_vertices=4)
		self.assertFalse(self.face == other2)

	def test_center_property(self):
		# Should raise TypeError due to incorrect property usage
		with self.assertRaises(TypeError):
			_ = self.face.center(self.vertices2d)

	def test_center_setter(self):
		from comgeo.core.vertex import Vertex2D
		v = Vertex2D(0.5, 0.5)
		self.face.center = v
		self.assertEqual(self.face._center, v)

	def test_area_property_not_implemented(self):
		with self.assertRaises(NotImplementedError):
			self.face.area(self.vertices2d)

	def test_area_setter_not_implemented(self):
		with self.assertRaises(NotImplementedError):
			self.face.set_area(1.0)

	def test_is_convex(self):
		self.assertTrue(self.face_convex_1.is_convex(self.vertices2d_convex))
		self.assertTrue(self.face_convex_2.is_convex(self.vertices2d_convex))
		self.assertFalse(self.face_non_convex.is_convex(self.vertices2d_non_convex))

	def test_is_convex_not_implemented(self):
		# Should raise NotImplementedError for Vertex2D
		with self.assertRaises(NotImplementedError):
			self.face.is_convex(self.vertices3d)

	def test_is_convex_3d(self):
		# Should raise NotImplementedError due to is_ccw_3d not implemented
		face3d = Face([0, 1, 2], max_num_vertices=3)
		with self.assertRaises(NotImplementedError):
			face3d.is_convex(self.vertices3d)

	def test_point_cloud_sampling_not_implemented(self):
		with self.assertRaises(NotImplementedError):
			self.face.point_cloud_sampling(10, self.vertices2d)

if __name__ == "__main__":
	unittest.main()
