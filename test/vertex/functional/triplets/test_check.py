import unittest
from comgeo.core.vertex import Vertex2D, Vertex3D
from comgeo.functional.vertex.triplets.check import is_ccw_2d, is_ccw_3d, is_ccw


class TestIsCCW2D(unittest.TestCase):
    """Test cases for is_ccw_2d function."""
    
    def test_ccw_points(self):
        """Test counter-clockwise points return True."""
        # Points forming a counter-clockwise turn: (0,0) -> (1,0) -> (1,1)
        v1 = Vertex2D(0, 0)
        v2 = Vertex2D(1, 0)
        v3 = Vertex2D(1, 1)
        self.assertTrue(is_ccw_2d(v1, v2, v3))
    
    def test_cw_points(self):
        """Test clockwise points return False."""
        # Points forming a clockwise turn: (0,0) -> (1,0) -> (1,-1)
        v1 = Vertex2D(0, 0)
        v2 = Vertex2D(1, 0)
        v3 = Vertex2D(1, -1)
        self.assertFalse(is_ccw_2d(v1, v2, v3))
    
    def test_colinear_points(self):
        """Test colinear points return False."""
        # Colinear points: (0,0) -> (1,0) -> (2,0)
        v1 = Vertex2D(0, 0)
        v2 = Vertex2D(1, 0)
        v3 = Vertex2D(2, 0)
        self.assertFalse(is_ccw_2d(v1, v2, v3))


class TestIsCCW3D(unittest.TestCase):
    """Test cases for is_ccw_3d function."""
    
    def test_raises_not_implemented(self):
        """Test that is_ccw_3d raises NotImplementedError."""
        v1 = Vertex3D(0, 0, 1)
        v2 = Vertex3D(1, 0, 2)
        v3 = Vertex3D(1, 1, 3)
        with self.assertRaises(NotImplementedError):
            is_ccw_3d(v1, v2, v3)


class TestIsCCW(unittest.TestCase):
    """Test cases for the generic is_ccw function."""
    
    def test_2d_points(self):
        """Test with 2D points."""
        v1 = Vertex2D(0, 0)
        v2 = Vertex2D(1, 0)
        v3 = Vertex2D(1, 1)
        self.assertTrue(is_ccw(v1, v2, v3))
    
    def test_3d_points_raises_not_implemented(self):
        """Test that is_ccw with 3D points raises NotImplementedError."""
        v1 = Vertex3D(0, 0, 1)
        v2 = Vertex3D(1, 0, 2)
        v3 = Vertex3D(1, 1, 3)
        with self.assertRaises(NotImplementedError):
            is_ccw(v1, v2, v3)
    
    def test_mixed_types_raises_error(self):
        """Test that mixing 2D and 3D points raises an error."""
        v1 = Vertex2D(0, 0)
        v2 = Vertex3D(1, 0, 0)
        v3 = Vertex2D(1, 1)
        with self.assertRaises(AssertionError):
            is_ccw(v1, v2, v3)
    
    def test_custom_vertex2d_subclass_works(self):
        """Test that Vertex2D subclasses work with is_ccw."""
        class CustomVertex(Vertex2D):
            pass
            
        # Points forming a counter-clockwise turn: (0,0) -> (1,0) -> (1,1)
        v1 = CustomVertex(0, 0)
        v2 = CustomVertex(1, 0)
        v3 = CustomVertex(1, 1)
        self.assertTrue(is_ccw(v1, v2, v3))


if __name__ == '__main__':
    unittest.main()