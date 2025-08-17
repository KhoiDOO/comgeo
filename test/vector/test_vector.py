import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from comgeo.core.vector import Vector

class TestVector(unittest.TestCase):
    """Test cases for the base Vector class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.vec1 = Vector(id=1, visited=False)
        self.vec2 = Vector(id=2, visited=True)
        self.vec3 = Vector(id=1, visited=True)  # Same ID as vec1, different visited state

    def test_vector_initialization_default(self):
        """Test Vector initialization with default parameters."""
        vec = Vector()
        self.assertEqual(vec.id, -1)
        self.assertEqual(vec.visited, False)

    def test_vector_initialization_with_parameters(self):
        """Test Vector initialization with specific parameters."""
        vec = Vector(id=5, visited=True)
        self.assertEqual(vec.id, 5)
        self.assertEqual(vec.visited, True)

    def test_vector_id_property(self):
        """Test the id property getter and setter."""
        self.assertEqual(self.vec1.id, 1)
        
        # Test setter
        self.vec1.id = 10
        self.assertEqual(self.vec1.id, 10)

    def test_vector_visited_property(self):
        """Test the visited property getter and setter."""
        self.assertEqual(self.vec1.visited, False)
        self.assertEqual(self.vec2.visited, True)
        
        # Test setter
        self.vec1.visited = True
        self.assertEqual(self.vec1.visited, True)

    def test_vector_repr(self):
        """Test the string representation of Vector."""
        expected = "Vector(id=1, visited=False)"
        self.assertEqual(repr(self.vec1), expected)

    def test_vector_equality_same_id(self):
        """Test equality comparison between vectors with same ID."""
        self.assertEqual(self.vec1, self.vec3)  # Same ID, different visited state

    def test_vector_equality_different_id(self):
        """Test equality comparison between vectors with different IDs."""
        self.assertNotEqual(self.vec1, self.vec2)

    def test_vector_equality_with_non_vector(self):
        """Test equality comparison with non-Vector objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vec1 == "not a vector"
        self.assertIn("__eq__ is only supported for Vector instances", str(context.exception))

    def test_vector_less_than_not_implemented(self):
        """Test that less than comparison raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vec1 < self.vec2
        self.assertIn("__lt__ is not implemented for Vector", str(context.exception))

    def test_vector_addition_not_implemented(self):
        """Test that addition raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vec1 + self.vec2
        self.assertIn("__add__ is not implemented for Vector", str(context.exception))

    def test_vector_subtraction_not_implemented(self):
        """Test that subtraction raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vec1 - self.vec2
        self.assertIn("__sub__ is not implemented for Vector", str(context.exception))
    
    def test_vector_norm_not_implemented(self):
        """Test that norm raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vec1.norm()
        self.assertIn("norm is not implemented for Vector", str(context.exception))

if __name__ == '__main__':
    unittest.main()