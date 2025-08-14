import pytest
import math
from comgeo.core.vector import Vector, Vector2D, Vector3D
from comgeo.core.vertex import Vertex2D, Vertex3D

class TestVectorEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_zero_vectors(self):
        """Test operations with zero vectors."""
        zero2d = Vector2D(x=0.0, y=0.0)
        zero3d = Vector3D(x=0.0, y=0.0, z=0.0)
        
        assert zero2d.norm() == 0.0
        assert zero3d.norm() == 0.0
        
        vec2d = Vector2D(x=1.0, y=2.0)
        vec3d = Vector3D(x=1.0, y=2.0, z=3.0)
        
        result2d = vec2d + zero2d
        assert result2d._x == 1.0 and result2d._y == 2.0
        
        result3d = vec3d + zero3d
        assert result3d._x == 1.0 and result3d._y == 2.0 and result3d._z == 3.0
    
    def test_large_numbers(self):
        """Test with large coordinate values."""
        vec2d = Vector2D(x=1e10, y=1e10)
        vec3d = Vector3D(x=1e10, y=1e10, z=1e10)
        
        # Should not raise overflow errors
        norm2d = vec2d.norm()
        norm3d = vec3d.norm()
        
        assert norm2d > 0
        assert norm3d > 0
    
    def test_very_small_numbers(self):
        """Test with very small coordinate values."""
        vec2d = Vector2D(x=1e-10, y=1e-10)
        vec3d = Vector3D(x=1e-10, y=1e-10, z=1e-10)
        
        # Should not raise underflow errors
        norm2d = vec2d.norm()
        norm3d = vec3d.norm()
        
        assert norm2d >= 0
        assert norm3d >= 0