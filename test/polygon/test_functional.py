import unittest
from comgeo.core.vertex import Vertex2D, Vertex3D
from comgeo.functional.polygon.area import (
    get_triangle_area,
    get_quadrilateral_area,
    get_area
)
from comgeo.functional.polygon.center import get_center

class TestPolygonArea(unittest.TestCase):
    def test_get_center_2d(self):
        """Test center calculation for 2D vertices."""  
        vertices = [
            Vertex2D(0.0, 0.0),
            Vertex2D(4.0, 0.0),
            Vertex2D(4.0, 4.0),
            Vertex2D(0.0, 4.0)
        ]
        center = get_center(vertices)
        self.assertIsInstance(center, Vertex2D)
        self.assertEqual(center.x, 2.0)
        self.assertEqual(center.y, 2.0)

    def test_get_center_3d(self):
        """Test center calculation for 3D vertices."""
        vertices = [
            Vertex3D(0.0, 0.0, 0.0),
            Vertex3D(2.0, 0.0, 0.0),
            Vertex3D(2.0, 2.0, 2.0),
            Vertex3D(0.0, 2.0, 2.0)
        ]
        center = get_center(vertices)
        self.assertIsInstance(center, Vertex3D)
        self.assertEqual(center.x, 1.0)
        self.assertEqual(center.y, 1.0)
        self.assertEqual(center.z, 1.0)

    def test_triangle_area_2d(self):
        """Test area calculation for 2D triangle."""
        triangle = [
            Vertex2D(0.0, 0.0),
            Vertex2D(3.0, 0.0),
            Vertex2D(0.0, 4.0)
        ]
        area = get_triangle_area(triangle)
        self.assertAlmostEqual(area, 6.0)

    def test_triangle_area_3d(self):
        """Test area calculation for 3D triangle."""
        triangle = [
            Vertex3D(0.0, 0.0, 0.0),
            Vertex3D(3.0, 0.0, 0.0),
            Vertex3D(0.0, 4.0, 0.0)
        ]
        area = get_triangle_area(triangle)
        self.assertAlmostEqual(area, 6.0)

    def test_quadrilateral_area_2d(self):
        """Test area calculation for 2D quadrilateral."""
        quad = [
            Vertex2D(0.0, 0.0),
            Vertex2D(4.0, 0.0),
            Vertex2D(4.0, 3.0),
            Vertex2D(0.0, 3.0)
        ]
        area = get_quadrilateral_area(quad)
        self.assertAlmostEqual(area, 12.0)

    def test_quadrilateral_area_3d(self):
        """Test area calculation for 3D quadrilateral."""
        quad = [
            Vertex3D(0.0, 0.0, 0.0),
            Vertex3D(4.0, 0.0, 0.0),
            Vertex3D(4.0, 3.0, 0.0),
            Vertex3D(0.0, 3.0, 0.0)
        ]
        area = get_quadrilateral_area(quad)
        self.assertAlmostEqual(area, 12.0)

    def test_get_area_triangle(self):
        """Test get_area with triangle input."""
        triangle = [
            Vertex2D(0.0, 0.0),
            Vertex2D(3.0, 0.0),
            Vertex2D(0.0, 4.0)
        ]
        area = get_area(triangle)
        self.assertAlmostEqual(area, 6.0)

    def test_get_area_quadrilateral(self):
        """Test get_area with quadrilateral input."""
        quad = [
            Vertex2D(0.0, 0.0),
            Vertex2D(4.0, 0.0),
            Vertex2D(4.0, 3.0),
            Vertex2D(0.0, 3.0)
        ]
        area = get_area(quad)
        self.assertAlmostEqual(area, 12.0)

    def test_invalid_vertex_count(self):
        """Test with invalid number of vertices."""
        with self.assertRaises(ValueError):
            get_area([Vertex2D(0.0, 0.0), Vertex2D(1.0, 1.0)])  # Too few
        with self.assertRaises(ValueError):
            get_area([Vertex2D(float(i), float(i)) for i in range(5)])  # Too many

    def test_mixed_vertex_types(self):
        """Test with mixed vertex types."""
        with self.assertRaises(TypeError) as exc_info:
            get_area([
                Vertex2D(0.0, 0.0),
                Vertex3D(1.0, 0.0, 0.0),
                Vertex2D(0.0, 1.0)
            ])
        self.assertIn("All arguments must be of the same type for vertices", str(exc_info.exception))

    def test_non_vertex_input(self):
        """Test with non-vertex input."""
        with self.assertRaises(TypeError) as exc_info:
            get_area([(0, 0), (1, 0), (0, 1)])  # Not Vertex objects
        self.assertIn("Expected (<class 'comgeo.core.vertex.vertex2d.Vertex2D'>, <class 'comgeo.core.vertex.vertex3d.Vertex3D'>) for vertices, got <class 'tuple'>", str(exc_info.exception))

if __name__ == '__main__':
    unittest.main()