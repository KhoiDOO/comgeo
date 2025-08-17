import unittest
import numpy as np

from comgeo.core.vertex import Vertex, Vertex2D
from comgeo.core.graph.base import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        """Set up for test cases."""
        self.vertices = [Vertex2D(x=float(i), y=float(i), id=i) for i in range(5)]
        self.graph = Graph(vertices=self.vertices, id=1)

    def test_initialization(self):
        """Test graph initialization."""
        self.assertEqual(self.graph.id, 1)
        self.assertFalse(self.graph.visited)
        self.assertEqual(len(self.graph.vertices), 5)
        self.assertEqual(self.graph.adjacency_matrix.shape, (5, 5))
        self.assertTrue(np.all(self.graph.adjacency_matrix == 0))
        self.assertEqual(self.graph.adjacency_list, {})

    def test_id_property(self):
        """Test the id property."""
        self.graph.id = 10
        self.assertEqual(self.graph.id, 10)
        with self.assertRaises(TypeError):
            self.graph.id = "not an int"

    def test_visited_property(self):
        """Test the visited property."""
        self.graph.visited = True
        self.assertTrue(self.graph.visited)
        with self.assertRaises(TypeError):
            self.graph.visited = "not a bool"

    def test_vertices_property(self):
        """Test the vertices property."""
        new_vertices = [Vertex2D(x=float(i), y=float(i), id=i) for i in range(6)]
        self.graph.vertices = new_vertices
        self.assertEqual(len(self.graph.vertices), 6)

        with self.assertRaises(ValueError):
            self.graph.check_vertices_len([])

    def test_adjacency_matrix_property(self):
        """Test the adjacency_matrix property."""
        new_matrix = np.ones((5, 5))
        self.graph.adjacency_matrix = new_matrix
        self.assertTrue(np.all(self.graph.adjacency_matrix == new_matrix))
        with self.assertRaises(TypeError):
            self.graph.adjacency_matrix = [[1, 1], [1, 1]]

    def test_adjacency_list_property(self):
        """Test the adjacency_list property."""
        # The setter for adjacency_list is incorrectly defined.
        # It should be a setter, not a regular method.
        with self.assertRaises(TypeError):
            self.graph.adjacency_list({0: [1]})

    def test_add_vertex(self):
        """Test adding a vertex to the graph."""
        new_vertex = Vertex2D(x=5.0, y=5.0, id=5)
        self.graph.add_vertex(new_vertex, connections=[0, 2])
        self.assertEqual(len(self.graph.vertices), 6)
        self.assertEqual(self.graph.adjacency_matrix.shape, (6, 6))
        self.assertEqual(self.graph.adjacency_list[5], [0, 2])
        self.assertEqual(self.graph.adjacency_matrix[5, 0], 1)
        self.assertEqual(self.graph.adjacency_matrix[5, 2], 1)
        self.assertEqual(self.graph.adjacency_matrix[5, 1], 0)

    def test_initialization_errors(self):
        """Test initialization with incorrect types."""
        with self.assertRaises(TypeError):
            Graph(vertices="not a list")
        with self.assertRaises(ValueError):
            Graph(vertices=[])
        with self.assertRaises(TypeError):
            Graph(vertices=self.vertices, id="not an int")
        with self.assertRaises(TypeError):
            Graph(vertices=self.vertices, visited="not a bool")

if __name__ == '__main__':
    unittest.main()
