import unittest
import math
from comgeo.core.vector import Vector3D
from comgeo.core.vertex import Vertex3D
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class TestVector3D(unittest.TestCase):
    """Test cases for the Vector3D class."""

    def test_vector3d_init(self):
        """Test Vector3D initialization."""
        vec = Vector3D(x=3.0, y=4.0, z=5.0, id=1, visited=True)
        self.assertIsInstance(vec, Vector3D)
        self.assertEqual(vec._x, 3.0)
        self.assertEqual(vec._y, 4.0)
        self.assertEqual(vec._z, 5.0)
        self.assertEqual(vec.id, 1)
        self.assertEqual(vec.visited, True)

    def test_vector3d_init_default(self):
        """Test Vector3D initialization with default values."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0)
        self.assertIsInstance(vec, Vector3D)
        self.assertEqual(vec._x, 1.0)
        self.assertEqual(vec._y, 2.0)
        self.assertEqual(vec._z, 3.0)
        self.assertEqual(vec.id, -1)
        self.assertEqual(vec.visited, False)

    def test_vector3d_init_custom(self):
        """Test Vector3D initialization with custom values."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=5, visited=True)
        self.assertIsInstance(vec, Vector3D)
        self.assertEqual(vec._x, 1.0)
        self.assertEqual(vec._y, 2.0)
        self.assertEqual(vec._z, 3.0)
        self.assertEqual(vec.id, 5)
        self.assertEqual(vec.visited, True)

    def test_vector3d_from_vertices(self):
        """Test creating Vector3D from two Vertex3D instances."""
        v1 = Vertex3D(x=1.0, y=2.0, z=3.0)
        v2 = Vertex3D(x=4.0, y=6.0, z=9.0)
        vec = Vector3D.from_vertices(v1, v2, id=5, visited=True)
        
        self.assertIsInstance(vec, Vector3D)
        self.assertEqual(vec._x, 3.0)  # 4.0 - 1.0
        self.assertEqual(vec._y, 4.0)  # 6.0 - 2.0
        self.assertEqual(vec._z, 6.0)  # 9.0 - 3.0
        self.assertEqual(vec.id, 5)
        self.assertEqual(vec.visited, True)

    def test_vector3d_from_vertices_error(self):
        """Test from_vertices raises error with wrong types."""
        v1 = Vertex3D(x=1.0, y=2.0, z=3.0)
        
        with self.assertRaises(TypeError):
            Vector3D.from_vertices(v1, "not_vertex", id=1)
        
        with self.assertRaises(TypeError):
            Vector3D.from_vertices("not_vertex", v1, id=1)

    def test_vector3d_from_vertex(self):
        """Test creating Vector3D from a single Vertex3D."""
        v = Vertex3D(x=1.0, y=2.0, z=3.0)
        vec = Vector3D.from_vertex(v)
        
        self.assertIsInstance(vec, Vector3D)
        self.assertEqual(vec._x, 1.0)
        self.assertEqual(vec._y, 2.0)
        self.assertEqual(vec._z, 3.0)

    def test_vector3d_from_vertex_error(self):
        """Test from_vertex raises error with wrong type."""
        with self.assertRaises(AttributeError):
            Vector3D.from_vertex("not_vertex")

    def test_vector3d_repr(self):
        """Test string representation."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=4, visited=False)
        expected = "Vector3D(x=1.0, y=2.0, z=3.0, id=4, visited=False)"
        self.assertEqual(repr(vec), expected)

    def test_vector3d_equality(self):
        """Test equality based on coordinates."""
        vec1 = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        vec2 = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        vec3 = Vector3D(x=1.0, y=2.0, z=4.0, id=1, visited=True)
        
        self.assertTrue(vec1 == vec2)
        self.assertFalse(vec1 == vec3)
    
    def test_vector3d_equality_error(self):
        """Test equality raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec == "string"
        self.assertIn("__eq__ is only supported for Vector3D instances", str(exc_info.exception))

    def test_vector3d_less_than(self):
        """Test less than comparison."""
        vec1 = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        vec2 = Vector3D(x=2.0, y=2.0, z=3.0, id=1, visited=True)
        vec3 = Vector3D(x=1.0, y=3.0, z=3.0, id=1, visited=True)
        
        self.assertTrue(vec1 < vec2)
        self.assertTrue(vec1 < vec3)
        self.assertFalse(vec2 < vec1)
    
    def test_vector3d_less_than_error(self):
        """Test less than raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec < "string"
        self.assertIn("__lt__ is only supported for Vector3D instances", str(exc_info.exception))

    def test_vector3d_addition(self):
        """Test vector addition."""
        vec1 = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        vec2 = Vector3D(x=4.0, y=5.0, z=6.0, id=1, visited=True)
        result = vec1 + vec2
        
        self.assertIsInstance(result, Vector3D)
        self.assertEqual(result, Vector3D(x=5.0, y=7.0, z=9.0))

    def test_vector3d_addition_error(self):
        """Test addition raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec + "not_vector"
        self.assertIn("__add__ is only supported for Vector3D instances", str(exc_info.exception))

    def test_vector3d_subtraction(self):
        """Test vector subtraction."""
        vec1 = Vector3D(x=5.0, y=7.0, z=9.0, id=1, visited=True)
        vec2 = Vector3D(x=2.0, y=3.0, z=4.0, id=1, visited=True)
        result = vec1 - vec2
        
        self.assertIsInstance(result, Vector3D)
        self.assertEqual(result, Vector3D(x=3.0, y=4.0, z=5.0))
    
    def test_vector3d_scalar_multiplication(self):
        """Test vector multiplication."""
        vec = Vector3D(x=2.0, y=3.0, z=4.0, id=1, visited=True)
        result = vec * 2.0
        
        self.assertIsInstance(result, Vector3D)
        self.assertEqual(result, Vector3D(x=4.0, y=6.0, z=8.0))
    
    def test_vector3d_scalar_multiplication_error(self):
        """Test multiplication raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec * "not_float"
        self.assertIn("__mul__ is only supported for float instances or Vector3D instances", str(exc_info.exception))
    
    def test_vector3d_dot_product(self):
        """Test dot product."""
        vec1 = Vector3D(x=1.0, y=1.0, z=1.0, id=1, visited=True)
        vec2 = Vector3D(x=3.0, y=4.0, z=6.0, id=1, visited=True)
        result = vec1 * vec2
        
        self.assertIsInstance(result, float)
        self.assertEqual(result, 13.0)

    def test_vector3d_scalar_division(self):
        """Test vector division."""
        vec = Vector3D(x=4.0, y=6.0, z=8.0, id=1, visited=True)
        result = vec / 2.0
        
        self.assertIsInstance(result, Vector3D)
        self.assertEqual(result, Vector3D(x=2.0, y=3.0, z=4.0))
    
    def test_vector3d_scalar_division_error(self):
        """Test division raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec / "not_float"
        self.assertIn("__truediv__ is only supported for float instances", str(exc_info.exception))
    
    def test_vector3d_scalar_division_zero(self):
        """Test division by zero."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(ValueError) as exc_info:
            vec / 0.0
        self.assertIn("Cannot divide by zero", str(exc_info.exception))
    
    def test_vector3d_cross_product(self):
        """Test cross product."""
        vec1 = Vector3D(x=1.0, y=1.0, z=1.0)
        vec2 = Vector3D(x=3.0, y=4.0, z=6.0)
        result = vec1.cross(vec2)
        
        self.assertIsInstance(result, Vector3D)
        self.assertEqual(result, Vector3D(x=2.0, y=-3.0, z=1.0))

    def test_vector3d_subtraction_error(self):
        """Test subtraction raises error with wrong type."""
        vec = Vector3D(x=1.0, y=2.0, z=3.0, id=1, visited=True)
        with self.assertRaises(TypeError) as exc_info:
            vec - "not_vector"
        self.assertIn("__sub__ is only supported for Vector3D instances", str(exc_info.exception))

    def test_vector3d_norm_default(self):
        """Test norm calculation with default p=2."""
        vec = Vector3D(x=2.0, y=3.0, z=6.0, id=1, visited=True)
        result = vec.norm()
        expected = math.sqrt(4 + 9 + 36)  # sqrt(2^2 + 3^2 + 6^2) = 7
        self.assertAlmostEqual(result, expected, delta=1e-10)

    def test_vector3d_norm_custom_p(self):
        """Test norm calculation with custom p value."""
        vec = Vector3D(x=1.0, y=1.0, z=1.0, id=1, visited=True)
        result = vec.norm(p=1)  # Manhattan norm
        expected = 3.0  # |1| + |1| + |1| = 3
        self.assertAlmostEqual(result, expected, delta=1e-10)

    def test_vector3d_norm_negative_values(self):
        """Test norm with negative coordinates."""
        vec = Vector3D(x=-2.0, y=-3.0, z=-6.0, id=1, visited=True)
        result = vec.norm()
        expected = 7.0  # Same as positive case due to absolute values
        self.assertAlmostEqual(result, expected, delta=1e-10)

    def test_vector3d_norm_error(self):
        """Test norm raises error with invalid p value."""
        vec = Vector3D(x=1.0, y=1.0, z=1.0, id=1, visited=True)
        with self.assertRaises(ValueError) as exc_info:
            vec.norm(p=0)
        self.assertIn("p must be a positive number", str(exc_info.exception))
        
        with self.assertRaises(ValueError) as exc_info:
            vec.norm(p=-1)
        self.assertIn("p must be a positive number", str(exc_info.exception))

    def test_vector3d_norm_type_error(self):
        """Test norm raises error with non-integer p value."""
        vec = Vector3D(x=1.0, y=1.0, z=1.0, id=1, visited=True)     
        with self.assertRaises(TypeError) as exc_info:
            vec.norm(p="not_int")
        self.assertIn("'<=' not supported between instances of 'str' and 'int'", str(exc_info.exception))