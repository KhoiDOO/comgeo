import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from comgeo.core.vertex import Vertex


class TestVertex(unittest.TestCase):
    """Test cases for the base Vertex class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.vertex1 = Vertex(id=1, visited=False)
        self.vertex2 = Vertex(id=2, visited=True)
        self.vertex3 = Vertex(id=1, visited=True)  # Same ID as vertex1, different visited state

    def test_vertex_initialization_default(self):
        """Test Vertex initialization with default parameters."""
        vertex = Vertex()
        self.assertEqual(vertex.id, -1)
        self.assertEqual(vertex.visited, False)

    def test_vertex_initialization_with_parameters(self):
        """Test Vertex initialization with specific parameters."""
        vertex = Vertex(id=5, visited=True)
        self.assertEqual(vertex.id, 5)
        self.assertEqual(vertex.visited, True)

    def test_vertex_id_property(self):
        """Test the id property getter and setter."""
        self.assertEqual(self.vertex1.id, 1)
        
        # Test setter
        self.vertex1.id = 10
        self.assertEqual(self.vertex1.id, 10)

    def test_vertex_visited_property(self):
        """Test the visited property getter and setter."""
        self.assertEqual(self.vertex1.visited, False)
        self.assertEqual(self.vertex2.visited, True)
        
        # Test setter
        self.vertex1.visited = True
        self.assertEqual(self.vertex1.visited, True)

    def test_vertex_repr(self):
        """Test the string representation of Vertex."""
        expected = "Vertex(id=1, visited=False)"
        self.assertEqual(repr(self.vertex1), expected)

    def test_vertex_equality_same_id(self):
        """Test equality comparison between vertices with same ID."""
        self.assertEqual(self.vertex1, self.vertex3)  # Same ID, different visited state

    def test_vertex_equality_different_id(self):
        """Test equality comparison between vertices with different IDs."""
        self.assertNotEqual(self.vertex1, self.vertex2)

    def test_vertex_equality_with_non_vertex(self):
        """Test equality comparison with non-Vertex objects raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.vertex1 == "not a vertex"
        self.assertIn("__eq__ is only supported for Vertex instances", str(context.exception))

    def test_vertex_less_than_not_implemented(self):
        """Test that less than comparison raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vertex1 < self.vertex2
        self.assertIn("__lt__ is not implemented for Vertex", str(context.exception))

    def test_vertex_addition_not_implemented(self):
        """Test that addition raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vertex1 + self.vertex2
        self.assertIn("__add__ is not implemented for Vertex", str(context.exception))

    def test_vertex_subtraction_not_implemented(self):
        """Test that subtraction raises NotImplementedError."""
        with self.assertRaises(NotImplementedError) as context:
            self.vertex1 - self.vertex2
        self.assertIn("__sub__ is not implemented for Vertex", str(context.exception))

if __name__ == '__main__':
    unittest.main()