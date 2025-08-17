import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from comgeo.core.vertex import Vertex3D


class TestVertex3D(unittest.TestCase):
    """Test cases for the Vertex3D class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.vertex1 = Vertex3D(1.0, 2.0, 3.0, id=1, visited=False)
        self.vertex2 = Vertex3D(4.0, 5.0, 6.0, id=2, visited=True)
        self.vertex3 = Vertex3D(1.0, 2.0, 3.0, id=3, visited=False)  # Same coordinates as vertex1

    def test_vertex3d_initialization_default_id_visited(self):
        """Test Vertex3D initialization with default id and visited parameters."""
        vertex = Vertex3D(5.0, 6.0, 7.0)
        self.assertEqual(vertex.x, 5.0)
        self.assertEqual(vertex.y, 6.0)
        self.assertEqual(vertex.z, 7.0)
        self.assertEqual(vertex.id, -1)
        self.assertEqual(vertex.visited, False)

    def test_vertex3d_initialization_all_parameters(self):
        """Test Vertex3D initialization with all parameters."""
        vertex = Vertex3D(1.5, 2.5, 3.5, id=10, visited=True)
        self.assertEqual(vertex.x, 1.5)
        self.assertEqual(vertex.y, 2.5)
        self.assertEqual(vertex.z, 3.5)
        self.assertEqual(vertex.id, 10)
        self.assertEqual(vertex.visited, True)

    def test_vertex3d_coordinates_property(self):
        """Test the coordinates property."""
        self.assertEqual(self.vertex1.coordinates, (1.0, 2.0, 3.0))
        self.assertEqual(self.vertex2.coordinates, (4.0, 5.0, 6.0))

    def test_vertex3d_set_coordinates(self):
        """Test the set_coordinates method."""
        self.vertex1.set_coordinates(10.0, 20.0, 30.0)
        self.assertEqual(self.vertex1.x, 10.0)
        self.assertEqual(self.vertex1.y, 20.0)
        self.assertEqual(self.vertex1.z, 30.0)
        self.assertEqual(self.vertex1.coordinates, (10.0, 20.0, 30.0))

    def test_vertex3d_xyz_properties(self):
        """Test the x, y, z property getters and setters."""
        # Test getters
        self.assertEqual(self.vertex1.x, 1.0)
        self.assertEqual(self.vertex1.y, 2.0)
        self.assertEqual(self.vertex1.z, 3.0)
        
        # Test setters
        self.vertex1.x = 15.0
        self.vertex1.y = 25.0
        self.vertex1.z = 35.0
        self.assertEqual(self.vertex1.x, 15.0)
        self.assertEqual(self.vertex1.y, 25.0)
        self.assertEqual(self.vertex1.z, 35.0)

    def test_vertex3d_repr(self):
        """Test the string representation of Vertex3D."""
        expected = "Vertex3D(x=1.0, y=2.0, z=3.0, id=1, visited=False)"
        self.assertEqual(repr(self.vertex1), expected)

    def test_vertex3d_equality_same_coordinates(self):
        """Test equality comparison between vertices with same coordinates."""
        self.assertEqual(self.vertex1, self.vertex3)

    def test_vertex3d_equality_different_coordinates(self):
        """Test equality comparison between vertices with different coordinates."""
        self.assertNotEqual(self.vertex1, self.vertex2)

    def test_vertex3d_equality_with_non_vertex3d(self):
        """Test equality comparison with non-Vertex3D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 == "not a vertex3d"
        self.assertIn("__eq__ is only supported for Vertex3D instances", str(context.exception))

    def test_vertex3d_less_than(self):
        """Test less than comparison between Vertex3D instances."""
        vertex_small = Vertex3D(0.0, 1.0, 2.0)
        vertex_large = Vertex3D(2.0, 3.0, 4.0)
        
        self.assertTrue(vertex_small < vertex_large)
        self.assertFalse(vertex_large < vertex_small)
        
        # Test lexicographic ordering
        vertex_same_xy = Vertex3D(1.0, 2.0, 2.0)
        self.assertTrue(vertex_same_xy < self.vertex1)  # (1.0, 2.0, 2.0) < (1.0, 2.0, 3.0)

    def test_vertex3d_less_than_with_non_vertex3d(self):
        """Test less than comparison with non-Vertex3D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 < "not a vertex3d"
        self.assertIn("__lt__ is only supported for Vertex3D instances", str(context.exception))

    def test_vertex3d_addition(self):
        """Test addition of two Vertex3D instances."""
        result = self.vertex1 + self.vertex2
        self.assertIsInstance(result, Vertex3D)
        self.assertEqual(result.x, 5.0)  # 1.0 + 4.0
        self.assertEqual(result.y, 7.0)  # 2.0 + 5.0
        self.assertEqual(result.z, 9.0)  # 3.0 + 6.0

    def test_vertex3d_addition_with_non_vertex3d(self):
        """Test addition with non-Vertex3D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 + "not a vertex3d"
        self.assertIn("__add__ is only supported for Vertex3D instances", str(context.exception))

    def test_vertex3d_subtraction(self):
        """Test subtraction of two Vertex3D instances."""
        result = self.vertex2 - self.vertex1
        self.assertIsInstance(result, Vertex3D)
        self.assertEqual(result.x, 3.0)  # 4.0 - 1.0
        self.assertEqual(result.y, 3.0)  # 5.0 - 2.0
        self.assertEqual(result.z, 3.0)  # 6.0 - 3.0
    
    def test_vertex3d_multiplication(self):
        """Test multiplication of a Vertex3D instance by a scalar."""
        result = self.vertex1 * 2.0
        self.assertIsInstance(result, Vertex3D)
        self.assertEqual(result.x, 2.0)  # 1.0 * 2
        self.assertEqual(result.y, 4.0)  # 2.0 * 2
        self.assertEqual(result.z, 6.0)  # 3.0 * 2
    
    def test_vertex3d_multiplication_with_non_float(self):
        """Test multiplication with non-float raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 * "not a float"
        self.assertIn("__mul__ is only supported for float instances", str(context.exception))
    
    def test_vertex3d_division(self):
        """Test division of a Vertex3D instance by a scalar."""
        result = self.vertex1 / 2.0
        self.assertIsInstance(result, Vertex3D)
        self.assertEqual(result.x, 0.5)  # 1.0 / 2
        self.assertEqual(result.y, 1.0)  # 2.0 / 2
        self.assertEqual(result.z, 1.5)  # 3.0 / 2
    
    def test_vertex3d_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.vertex1 / 0.0
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_vertex3d_division_by_non_float(self):
        """Test division by non-float raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 / "not a float"
        self.assertIn("__truediv__ is only supported for float instances", str(context.exception))

    def test_vertex3d_subtraction_with_non_vertex3d(self):
        """Test subtraction with non-Vertex3D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 - "not a vertex3d"
        self.assertIn("__sub__ is only supported for Vertex3D instances", str(context.exception))

    def test_vertex3d_distance_to(self):
        """Test distance calculation between two Vertex3D instances."""
        distance = self.vertex1.distance_to(self.vertex2)
        expected_distance = ((4.0 - 1.0) ** 2 + (5.0 - 2.0) ** 2 + (6.0 - 3.0) ** 2) ** 0.5
        self.assertAlmostEqual(distance, expected_distance, places=10)
        
        # Test distance to self
        self.assertEqual(self.vertex1.distance_to(self.vertex1), 0.0)

    def test_vertex3d_distance_to_with_non_vertex3d(self):
        """Test distance calculation with non-Vertex3D objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1.distance_to("not a vertex3d")
        self.assertIn("distance_to is only supported for Vertex3D instances", str(context.exception))

if __name__ == '__main__':
    unittest.main()