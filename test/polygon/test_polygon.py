import unittest
from comgeo.core.polygon.base import Polygon
from comgeo.core.vertex import Vertex, Vertex2D, Vertex3D


class TestPolygon(unittest.TestCase):
    """Test cases for the Polygon class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.vertices1 = [Vertex2D(0.0, 0.0), Vertex2D(1.0, 0.0), Vertex2D(1.0, 1.0), Vertex2D(0.0, 1.0)]
        self.vertices2 = [Vertex3D(0.0, 0.0, 0.0), Vertex3D(1.0, 0.0, 0.0), Vertex3D(1.0, 1.0, 0.0)]
        self.polygon1 = Polygon(self.vertices1, id=1, visited=False)
        self.polygon2 = Polygon(self.vertices2, id=2, visited=True)
        self.polygon3 = Polygon(self.vertices1, id=1, visited=False) # Same as polygon1
        self.polygon4 = Polygon(self.vertices1[::-1], id=1, visited=False) # Different order

    def test_polygon_initialization_default(self):
        """Test Polygon initialization with default parameters."""
        polygon = Polygon(self.vertices1)
        self.assertEqual(polygon.id, -1)
        self.assertEqual(polygon.visited, False)
        self.assertEqual(polygon.vertices, self.vertices1)

    def test_polygon_initialization_with_parameters(self):
        """Test Polygon initialization with specific parameters."""
        self.assertEqual(self.polygon1.id, 1)
        self.assertEqual(self.polygon1.visited, False)
        self.assertEqual(self.polygon1.vertices, self.vertices1)

    def test_id_property(self):
        """Test the id property getter and setter."""
        self.assertEqual(self.polygon1.id, 1)
        self.polygon1.id = 10
        self.assertEqual(self.polygon1.id, 10)

    def test_visited_property(self):
        """Test the visited property getter and setter."""
        self.assertEqual(self.polygon1.visited, False)
        self.polygon1.visited = True
        self.assertEqual(self.polygon1.visited, True)

    def test_vertices_property(self):
        """Test the vertices property getter and setter."""
        self.assertEqual(self.polygon1.vertices, self.vertices1)
        new_vertices = [Vertex2D(2.0, 2.0), Vertex2D(3.0, 2.0), Vertex2D(3.0, 3.0)]
        self.polygon1.vertices = new_vertices
        self.assertEqual(self.polygon1.vertices, new_vertices)

    def test_vertices_consistency_error(self):
        """Test that setting inconsistent vertex types raises TypeError."""
        inconsistent_vertices = [Vertex2D(0.0, 0.0), Vertex3D(1.0, 1.0, 1.0)]
        with self.assertRaises(TypeError) as context:
            Polygon(inconsistent_vertices)
        self.assertIn("All arguments must be of the same type for vertices", str(context.exception))

        with self.assertRaises(TypeError) as context:
            self.polygon1.vertices = inconsistent_vertices
        self.assertIn("All arguments must be of the same type for vertices", str(context.exception))

    def test_polygon_equality(self):
        """Test polygon equality."""
        self.assertEqual(self.polygon1, self.polygon3)
        self.assertNotEqual(self.polygon1, self.polygon2)

    def test_polygon_equality_with_non_polygon(self):
        """Test equality with a non-Polygon object raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.polygon1 == "not a polygon"
        self.assertIn("__eq__ is only supported for Polygon instances.", str(context.exception))

    def test_repr_and_str(self):
        """Test the __repr__ and __str__ methods."""
        expected_repr = f"Polygon(id={self.polygon1.id}, visited={self.polygon1.visited}, \nvertices={self.polygon1.vertices})"
        self.assertEqual(repr(self.polygon1), expected_repr)
        self.assertEqual(str(self.polygon1), expected_repr)

    def test_is_convex(self):
        """Test the is_convex method for a convex polygon."""
        self.assertTrue(self.polygon1.is_convex())
        self.assertTrue(self.polygon4.is_convex())

    def test_is_not_convex(self):
        """Test the is_convex method for a non-convex polygon."""
        non_convex_vertices = [Vertex2D(0.0, 0.0), Vertex2D(2.0, 0.0), Vertex2D(1.0, 1.0), Vertex2D(2.0, 2.0), Vertex2D(0.0, 2.0)]
        non_convex_polygon = Polygon(non_convex_vertices)
        self.assertFalse(non_convex_polygon.is_convex())

    def test_is_convex_not_implemented_for_3d(self):
        """Test that is_convex raises NotImplementedError for 3D vertices."""
        with self.assertRaises(NotImplementedError) as context:
            self.polygon2.is_convex()
        self.assertIn("is_convex not implemented for <class 'comgeo.core.vertex.vertex3d.Vertex3D'>", str(context.exception))

    def test_point_cloud_sampling_not_implemented(self):
        """Test that point_cloud_sampling raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.polygon1.point_cloud_sampling(10)
        self.assertIn("point_cloud_sampling is not implemented for Polygon", str(context.exception))

if __name__ == '__main__':
    unittest.main()
