import unittest
from comgeo.core.vertex import Vertex2D, Vertex3D
from comgeo.core.mesh.edges.base import BaseEdge, BaseEdge2D, BaseEdge3D

class TestBaseEdge(unittest.TestCase):
    def setUp(self):
        self.v1 = Vertex2D(0.0, 0.0)
        self.v2 = Vertex2D(3.0, 4.0)
        self.v3 = Vertex2D(1.0, 1.0)
        self.v4 = Vertex2D(4.0, 0.0)
        self.e1 = BaseEdge(self.v1, self.v2)
        self.e2 = BaseEdge(self.v3, self.v4)
        self.e2d = BaseEdge2D(self.v1, self.v2)
        self.v1_3d = Vertex3D(0.0, 0.0, 0.0)
        self.v2_3d = Vertex3D(1.0, 2.0, 2.0)
        self.e3d = BaseEdge3D(self.v1_3d, self.v2_3d)

    def test_properties(self):
        self.assertEqual(self.e1.start, self.v1)
        self.assertEqual(self.e1.end, self.v2)
        self.assertEqual(self.e2d.start, self.v1)
        self.assertEqual(self.e2d.end, self.v2)
        self.assertEqual(self.e3d.start, self.v1_3d)
        self.assertEqual(self.e3d.end, self.v2_3d)

    def test_length(self):
        self.assertAlmostEqual(self.e1.length(), 5.0)
        self.assertAlmostEqual(self.e2d.length(), 5.0)
        self.assertAlmostEqual(self.e3d.length(), 3.0)

    def test_repr_str(self):
        self.assertIn("BaseEdge", repr(self.e1))
        self.assertIn("start=", repr(self.e1))
        self.assertTrue(str(self.e1).startswith("[["))

    def test_intersect(self):
        # These two edges should intersect
        edge1 = BaseEdge(Vertex2D(0.0, 0.0), Vertex2D(4.0, 4.0))
        edge2 = BaseEdge(Vertex2D(0.0, 4.0), Vertex2D(4.0, 0.0))
        self.assertTrue(edge1.intersect(edge2))
        # These two edges should not intersect
        edge3 = BaseEdge(Vertex2D(0.0, 0.0), Vertex2D(1.0, 1.0))
        edge4 = BaseEdge(Vertex2D(2.0, 2.0), Vertex2D(3.0, 3.0))
        self.assertFalse(edge3.intersect(edge4))

if __name__ == "__main__":
    unittest.main()
