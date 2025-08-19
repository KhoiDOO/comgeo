import unittest
from comgeo.core.polygon.triangle import Triangle
from comgeo.core.vertex import Vertex, Vertex2D, Vertex3D


class TestTriangle(unittest.TestCase):
    """Test cases for the Triangle class."""

    def setUp(self):
        """Set up test fixtures."""
        self.vertices2d = [Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0), Vertex2D(0.0, 1.0)]
        self.vertices3d = [Vertex3D(0.0, 0.0, 0.0), Vertex3D(1.0, 0.0, 0.0), Vertex3D(0.0, 1.0, 0.0)]
        self.triangle2d = Triangle(self.vertices2d, id=1)
        self.triangle3d = Triangle(self.vertices3d, id=2)

    def test_triangle_initialization(self):
        """Test Triangle initialization."""
        self.assertEqual(self.triangle2d.id, 1)
        self.assertEqual(len(self.triangle2d.vertices), 3)

    def test_triangle_initialization_invalid_vertices(self):
        """Test Triangle initialization with an invalid number of vertices."""
        with self.assertRaises(ValueError) as context:
            Triangle([Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0)])
        self.assertIn("Triangle must have 3 vertices", str(context.exception))

    def test_vertices_setter(self):
        """Test the vertices property setter."""
        new_vertices = [Vertex2D(1.0, 1.0), Vertex2D(2.0, 1.0), Vertex2D(1.0, 2.0)]
        self.triangle2d.vertices = new_vertices
        self.assertEqual(self.triangle2d.vertices, new_vertices)

    def test_vertices_setter_invalid(self):
        """Test the vertices property setter with an invalid number of vertices."""
        with self.assertRaises(ValueError) as context:
            self.triangle2d.vertices = [Vertex2D(0.0, 0.0)]
        self.assertIn("Triangle must have 3 vertices", str(context.exception))

    def test_repr_and_str(self):
        """Test the __repr__ and __str__ methods."""
        expected_repr = f"Triangle(id={self.triangle2d.id}, visited={self.triangle2d.visited}, \nvertices={self.triangle2d.vertices})"
        self.assertEqual(repr(self.triangle2d), expected_repr)
        self.assertEqual(str(self.triangle2d), expected_repr)

    def test_is_convex_not_implemented(self):
        """Test that is_convex raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.triangle2d.is_convex()
        self.assertIn("is_convex is not implemented for Triangle", str(context.exception))

    def test_point_cloud_sampling_2d(self):
        """Test point cloud sampling for a 2D triangle."""
        num_points = 10
        points = self.triangle2d.point_cloud_sampling(num_points)
        self.assertEqual(len(points), num_points)
        for point in points:
            self.assertIsInstance(point, Vertex2D)

    def test_point_cloud_sampling_3d(self):
        """Test point cloud sampling for a 3D triangle."""
        num_points = 10
        points = self.triangle3d.point_cloud_sampling(num_points)
        self.assertEqual(len(points), num_points)
        for point in points:
            self.assertIsInstance(point, Vertex3D)

    def test_point_cloud_sampling_base_vertex_error(self):
        """Test Triangle construction raises error for base Vertex."""
        base_vertices = [Vertex(id=1), Vertex(id=2), Vertex(id=3)]
        with self.assertRaises(ValueError) as context:
            Triangle(base_vertices)
        self.assertIn("Polygon must have vertices of type Vertex2D or Vertex3D", str(context.exception))

if __name__ == '__main__':
    unittest.main()
