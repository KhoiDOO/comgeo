import unittest
from comgeo.core.polygon.quad import Quad
from comgeo.core.vertex import Vertex, Vertex2D, Vertex3D


class TestQuad(unittest.TestCase):
    """Test cases for the Quad class."""

    def setUp(self):
        """Set up test fixtures."""
        self.vertices = [
            Vertex2D(0.0, 0.0),
            Vertex2D(1.0, 0.0),
            Vertex2D(1.0, 1.0),
            Vertex2D(0.0, 1.0)
        ]
        self.quad = Quad(self.vertices, id=1)
        self.non_convex_vertices = [
            Vertex2D(0.0, 0.0),
            Vertex2D(2.0, 0.0),
            Vertex2D(1.0, 1.0),
            Vertex2D(0.0, 2.0)
        ]
        self.non_convex_quad = Quad(self.non_convex_vertices, id=2)
        self.vertices3d = [
            Vertex3D(0.0, 0.0, 0.0),
            Vertex3D(1.0, 0.0, 0.0),
            Vertex3D(1.0, 1.0, 0.0),
            Vertex3D(0.0, 1.0, 0.0)
        ]
        self.quad3d = Quad(self.vertices3d, id=3)

    def test_quad_initialization(self):
        """Test Quad initialization."""
        self.assertEqual(self.quad.id, 1)
        self.assertEqual(len(self.quad.vertices), 4)

    def test_quad_initialization_invalid_vertices(self):
        """Test Quad initialization with an invalid number of vertices."""
        with self.assertRaises(ValueError) as context:
            Quad([Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0)])
        self.assertIn("Quad must have 4 vertices", str(context.exception))

    def test_vertices_setter(self):
        """Test the vertices property setter."""
        new_vertices = [
            Vertex2D(1.0, 1.0),
            Vertex2D(2.0, 1.0),
            Vertex2D(2.0, 2.0),
            Vertex2D(1.0, 2.0)
        ]
        self.quad.vertices = new_vertices
        self.assertEqual(self.quad.vertices, new_vertices)

    def test_vertices_setter_invalid(self):
        """Test the vertices property setter with an invalid number of vertices."""
        with self.assertRaises(ValueError) as context:
            self.quad.vertices = [Vertex2D(0.0, 0.0)]
        self.assertIn("Quad must have 4 vertices", str(context.exception))

    def test_repr_and_str(self):
        """Test the __repr__ and __str__ methods."""
        expected_repr = f"Quad(id={self.quad.id}, visited={self.quad.visited}, \nvertices={self.quad.vertices})"
        self.assertEqual(repr(self.quad), expected_repr)
        self.assertEqual(str(self.quad), expected_repr)

    def test_is_convex(self):
        """Test the is_convex method."""
        self.assertTrue(self.quad.is_convex())
        self.assertFalse(self.non_convex_quad.is_convex())

    def test_point_cloud_sampling_2d(self):
        """Test point cloud sampling for a 2D quad."""
        num_points = 10
        points = self.quad.point_cloud_sampling(num_points)
        self.assertEqual(len(points), num_points)
        for point in points:
            self.assertIsInstance(point, Vertex2D)

    def test_point_cloud_sampling_3d(self):
        """Test point cloud sampling for a 3D quad."""
        num_points = 10
        points = self.quad3d.point_cloud_sampling(num_points)
        self.assertEqual(len(points), num_points)
        for point in points:
            self.assertIsInstance(point, Vertex3D)

    def test_point_cloud_sampling_base_vertex_error(self):
        """Test point cloud sampling raises error for base Vertex."""
        base_vertices = [Vertex(id=1), Vertex(id=2), Vertex(id=3), Vertex(id=4)]
        base_quad = Quad(base_vertices)
        with self.assertRaises(NotImplementedError) as context:
            base_quad.point_cloud_sampling(10)
        self.assertIn("point_cloud_sampling not implemented for", str(context.exception))

if __name__ == '__main__':
    unittest.main()
