import unittest
import math
from comgeo.core.vector import Vector2D
from comgeo.core.vertex import Vertex2D
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class TestVector2D(unittest.TestCase):
    """Test cases for the Vector2D class."""
    
    def test_vector2d_init(self):
        """Test Vector2D initialization."""
        vec = Vector2D(x=3.0, y=4.0, id=1, visited=True)
        assert vec._x == 3.0
        assert vec._y == 4.0
        assert vec.id == 1
        assert vec.visited == True
    
    def test_vector2d_init_default(self):
        """Test Vector2D initialization with default values."""
        vec = Vector2D(x=1.0, y=2.0)
        assert vec._x == 1.0
        assert vec._y == 2.0
        assert vec.id == -1
        assert vec.visited == False
    
    def test_vector2d_init_custom(self):
        """Test Vector2D initialization with custom values."""
        vec = Vector2D(x=1.0, y=2.0, id=5, visited=True)
        assert vec._x == 1.0
        assert vec._y == 2.0
        assert vec.id == 5
        assert vec.visited == True
    
    def test_vector2d_from_vertices(self):
        """Test creating Vector2D from two Vertex2D instances."""
        v1 = Vertex2D(x=1.0, y=2.0)
        v2 = Vertex2D(x=4.0, y=6.0)
        vec = Vector2D.from_vertices(v1, v2, id=5, visited=True)
        
        assert vec._x == 3.0  # 4.0 - 1.0
        assert vec._y == 4.0  # 6.0 - 2.0
        assert vec.id == 5
        assert vec.visited == True
    
    def test_vector2d_from_vertices_error(self):
        """Test from_vertices raises error with wrong types."""
        v1 = Vertex2D(x=1.0, y=2.0)
        
        with self.assertRaises(TypeError):
            Vector2D.from_vertices(v1, "not_vertex", id=1)
        
        with self.assertRaises(TypeError):
            Vector2D.from_vertices("not_vertex", v1, id=1)
    
    def test_vector2d_from_vertex(self):
        """Test creating Vector2D from a single Vertex2D."""
        v = Vertex2D(x=3.0, y=4.0)
        vec = Vector2D.from_vertex(v)
        
        assert vec._x == 3.0
        assert vec._y == 4.0
    
    def test_vector2d_from_vertex_error(self):
        """Test from_vertex raises error with wrong type."""
        with self.assertRaises(AttributeError):
            Vector2D.from_vertex("not_vertex")
    
    def test_vector2d_repr(self):
        """Test string representation."""
        vec = Vector2D(x=1.0, y=2.0, id=3, visited=True)
        expected = "Vector2D(x=1.0, y=2.0, id=3, visited=True)"
        assert repr(vec) == expected
    
    def test_vector2d_equality(self):
        """Test equality based on coordinates."""
        vec1 = Vector2D(x=1.0, y=2.0)
        vec2 = Vector2D(x=1.0, y=2.0)
        vec3 = Vector2D(x=2.0, y=3.0)
        
        assert vec1 == vec2
        assert not (vec1 == vec3)
    
    def test_vector2d_equality_error(self):
        """Test equality raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec == "string"
    
    def test_vector2d_less_than(self):
        """Test less than comparison."""
        vec1 = Vector2D(x=1.0, y=2.0)
        vec2 = Vector2D(x=2.0, y=3.0)
        vec3 = Vector2D(x=1.0, y=3.0)
        
        assert vec1 < vec2
        assert vec1 < vec3
        assert not (vec2 < vec1)
    
    def test_vector2d_less_than_error(self):
        """Test less than raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec < "string"
    
    def test_vector2d_addition(self):
        """Test vector addition."""
        vec1 = Vector2D(x=1.0, y=2.0)
        vec2 = Vector2D(x=3.0, y=4.0)
        result = vec1 + vec2
        
        assert result._x == 4.0
        assert result._y == 6.0
    
    def test_vector2d_addition_error(self):
        """Test addition raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec + "string"
    
    def test_vector2d_subtraction(self):
        """Test vector subtraction."""
        vec1 = Vector2D(x=5.0, y=7.0)
        vec2 = Vector2D(x=2.0, y=3.0)
        result = vec1 - vec2
        
        assert result._x == 3.0
        assert result._y == 4.0
    
    def test_vector2d_subtraction_error(self):
        """Test subtraction raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec - "string"
    
    def test_vector2d_multiplication(self):
        """Test vector multiplication."""
        vec = Vector2D(x=2.0, y=3.0)
        result = vec * 2.0
        
        assert result._x == 4.0
        assert result._y == 6.0
    
    def test_vector2d_multiplication_error(self):
        """Test multiplication raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec * "string"
    
    def test_vector2d_division(self):
        """Test vector division."""
        vec = Vector2D(x=4.0, y=6.0)
        result = vec / 2.0
        
        assert result._x == 2.0
        assert result._y == 3.0
    
    def test_vector2d_division_error(self):
        """Test division raises error with wrong type."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(TypeError):
            vec / "string"
    
    def test_vector2d_division_zero(self):
        """Test division by zero."""
        vec = Vector2D(x=1.0, y=2.0)
        with self.assertRaises(ValueError) as context:
            vec / 0.0
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_vector2d_norm_default(self):
        """Test norm calculation with default p=2."""
        vec = Vector2D(x=3.0, y=4.0)
        result = vec.norm()
        expected = math.sqrt(9 + 16)  # sqrt(3^2 + 4^2) = 5
        assert abs(result - expected) < 1e-10
    
    def test_vector2d_norm_custom_p(self):
        """Test norm calculation with custom p value."""
        vec = Vector2D(x=2.0, y=2.0)
        result = vec.norm(p=1)  # Manhattan norm
        expected = 4.0  # |2| + |2| = 4
        assert abs(result - expected) < 1e-10
        
        result = vec.norm(p=4)
        expected = (16 + 16) ** 0.25  # (2^4 + 2^4)^(1/4)
        assert abs(result - expected) < 1e-10
    
    def test_vector2d_norm_negative_values(self):
        """Test norm with negative coordinates."""
        vec = Vector2D(x=-3.0, y=-4.0)
        result = vec.norm()
        expected = 5.0  # Same as positive case due to absolute values
        assert abs(result - expected) < 1e-10

    def test_vector2d_norm_error(self):
        """Test norm raises error with invalid p value."""
        vec = Vector2D(x=1.0, y=1.0)
        with self.assertRaises(ValueError) as exc_info:
            vec.norm(p=0)
        self.assertIn("p must be a positive number", str(exc_info.exception))
        
        with self.assertRaises(ValueError) as exc_info:
            vec.norm(p=-1)
        self.assertIn("p must be a positive number", str(exc_info.exception))

    def test_vector2d_norm_type_error(self):
        """Test norm raises error with non-integer p value."""
        vec = Vector2D(x=1.0, y=1.0)     
        with self.assertRaises(TypeError) as exc_info:
            vec.norm(p="not_int")
        self.assertIn("'<=' not supported between instances of 'str' and 'int'", str(exc_info.exception))