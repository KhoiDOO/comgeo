import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from comgeo.core.vertex import Vertex2D

class TestVertex2D(unittest.TestCase):
    """Test cases for the Vertex2D class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.vertex1 = Vertex2D(1.0, 2.0, id=1, visited=False)
        self.vertex2 = Vertex2D(3.0, 4.0, id=2, visited=True)
        self.vertex3 = Vertex2D(1.0, 2.0, id=3, visited=False)  # Same coordinates as vertex1

    def test_vertex2d_initialization_default_id_visited(self):
        """Test Vertex2D initialization with default id and visited parameters."""
        vertex = Vertex2D(5.0, 6.0)
        self.assertEqual(vertex.x, 5.0)
        self.assertEqual(vertex.y, 6.0)
        self.assertEqual(vertex.id, -1)
        self.assertEqual(vertex.visited, False)

    def test_vertex2d_initialization_all_parameters(self):
        """Test Vertex2D initialization with all parameters."""
        vertex = Vertex2D(1.5, 2.5, id=10, visited=True)
        self.assertEqual(vertex.x, 1.5)
        self.assertEqual(vertex.y, 2.5)
        self.assertEqual(vertex.id, 10)
        self.assertEqual(vertex.visited, True)

    def test_vertex2d_coordinates_property(self):
        """Test the coordinates property."""
        self.assertEqual(self.vertex1.coordinates, (1.0, 2.0))
        self.assertEqual(self.vertex2.coordinates, (3.0, 4.0))

    def test_vertex2d_set_coordinates(self):
        """Test the set_coordinates method."""
        self.vertex1.set_coordinates(10.0, 20.0)
        self.assertEqual(self.vertex1.x, 10.0)
        self.assertEqual(self.vertex1.y, 20.0)
        self.assertEqual(self.vertex1.coordinates, (10.0, 20.0))

    def test_vertex2d_x_property(self):
        """Test the x property getter and setter."""
        self.assertEqual(self.vertex1.x, 1.0)
        
        # Test setter
        self.vertex1.x = 15.0
        self.assertEqual(self.vertex1.x, 15.0)

    def test_vertex2d_y_property(self):
        """Test the y property getter and setter."""
        self.assertEqual(self.vertex1.y, 2.0)
        
        # Test setter
        self.vertex1.y = 25.0
        self.assertEqual(self.vertex1.y, 25.0)

    def test_vertex2d_repr(self):
        """Test the string representation of Vertex2D."""
        expected = "Vertex2D(x=1.0, y=2.0, id=1, visited=False)"
        self.assertEqual(repr(self.vertex1), expected)

    def test_vertex2d_equality_same_coordinates(self):
        """Test equality comparison between vertices with same coordinates."""
        self.assertEqual(self.vertex1, self.vertex3)

    def test_vertex2d_equality_different_coordinates(self):
        """Test equality comparison between vertices with different coordinates."""
        self.assertNotEqual(self.vertex1, self.vertex2)

    def test_vertex2d_equality_with_non_vertex2d(self):
        """Test equality comparison with non-Vertex2D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 == "not a vertex2d"
        self.assertIn("__eq__ is only supported for Vertex2D instances", str(context.exception))

    def test_vertex2d_less_than(self):
        """Test less than comparison between Vertex2D instances."""
        vertex_small = Vertex2D(0.0, 1.0)
        vertex_large = Vertex2D(2.0, 3.0)
        
        self.assertTrue(vertex_small < vertex_large)
        self.assertFalse(vertex_large < vertex_small)
        
        # Test lexicographic ordering
        vertex_same_x = Vertex2D(1.0, 1.0)
        self.assertTrue(vertex_same_x < self.vertex1)  # (1.0, 1.0) < (1.0, 2.0)

    def test_vertex2d_less_than_with_non_vertex2d(self):
        """Test less than comparison with non-Vertex2D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 < "not a vertex2d"
        self.assertIn("__lt__ is only supported for Vertex2D instances", str(context.exception))

    def test_vertex2d_addition(self):
        """Test addition of two Vertex2D instances."""
        result = self.vertex1 + self.vertex2
        self.assertIsInstance(result, Vertex2D)
        self.assertEqual(result.x, 4.0)  # 1.0 + 3.0
        self.assertEqual(result.y, 6.0)  # 2.0 + 4.0

    def test_vertex2d_addition_with_non_vertex2d(self):
        """Test addition with non-Vertex2D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 + "not a vertex2d"
        self.assertIn("__add__ is only supported for Vertex2D instances", str(context.exception))

    def test_vertex2d_subtraction(self):
        """Test subtraction of two Vertex2D instances."""
        result = self.vertex2 - self.vertex1
        self.assertIsInstance(result, Vertex2D)
        self.assertEqual(result.x, 2.0)  # 3.0 - 1.0
        self.assertEqual(result.y, 2.0)  # 4.0 - 2.0

    def test_vertex2d_subtraction_with_non_vertex2d(self):
        """Test subtraction with non-Vertex2D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 - "not a vertex2d"
        self.assertIn("__sub__ is only supported for Vertex2D instances", str(context.exception))

    def test_vertex2d_distance_to(self):
        """Test distance calculation between two Vertex2D instances."""
        distance = self.vertex1.distance_to(self.vertex2)
        expected_distance = ((3.0 - 1.0) ** 2 + (4.0 - 2.0) ** 2) ** 0.5
        self.assertAlmostEqual(distance, expected_distance, places=10)
        
        # Test distance to self
        self.assertEqual(self.vertex1.distance_to(self.vertex1), 0.0)

    def test_vertex2d_distance_to_with_non_vertex2d(self):
        """Test distance calculation with non-Vertex2D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1.distance_to("not a vertex2d")
        self.assertIn("distance_to is only supported for Vertex2D instances", str(context.exception))

if __name__ == '__main__':
    unittest.main()