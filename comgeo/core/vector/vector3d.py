from .base import Vector
from ..vertex import Vertex3D

from ...decorator.error import not_self_instance, not_instance
from ..utils.error import check_type

import math

class Vector3D(Vector):
    def __init__(self, x: float, y: float, z: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        check_type(x, float, "x")
        check_type(y, float, "y")
        check_type(z, float, "z")

        self._x = x
        self._y = y
        self._z = z
    
    @property
    def coordinates(self):
        return self._x, self._y, self._z
    
    def set_coordinates(self, x: float, y: float, z: float):
        check_type(x, float, "x")
        check_type(y, float, "y")
        check_type(z, float, "z")
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    @not_instance(float)
    def x(self, value: float):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    @not_instance(float)
    def y(self, value: float):
        self._y = value
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    @not_instance(float)
    def z(self, value: float):
        self._z = value

    @staticmethod
    def from_vertices(v1: Vertex3D, v2: Vertex3D, id: int = -1, visited: bool = False) -> 'Vector3D':
        """Create a Vector3D from two Vertex3D instances."""
        if not isinstance(v1, Vertex3D) or not isinstance(v2, Vertex3D):
            raise TypeError("Both arguments must be Vertex3D instances.")
        return Vector3D(x=v2.x - v1.x, y=v2.y - v1.y, z=v2.z - v1.z, id=id, visited=visited)

    @staticmethod
    @not_instance(Vertex3D)
    def from_vertex(v: Vertex3D) -> 'Vector3D':
        """Create a Vector3D from a Vertex3D instance."""
        return Vector3D(x=v.x, y=v.y, z=v.z)

    def __repr__(self):
        return f"Vector3D(x={self._x}, y={self._y}, z={self._z}, id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other: 'Vector3D') -> bool:
        """Check equality based on the coordinates of the vector."""
        return self._x == other._x and self._y == other._y and self._z == other._z

    @not_self_instance
    def __lt__(self, other: 'Vector3D') -> bool:
        """Check if this vector is less than another vector."""
        return (self._x, self._y, self._z) < (other._x, other._y, other._z)

    @not_self_instance
    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        """Add two vectors."""
        return Vector3D(self._x + other._x, self._y + other._y, self._z + other._z)

    @not_self_instance
    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        """Subtract two vectors."""
        return Vector3D(self._x - other._x, self._y - other._y, self._z - other._z)
    
    def __mul__(self, other): 
        """Multiply a Vector3D instance by a scalar or another Vector3D."""
        if not isinstance(other, (float, Vector3D)):
            raise TypeError("__mul__ is only supported for float instances or Vector3D instances")
        if isinstance(other, Vector3D):
            return self._x * other._x + self._y * other._y + self._z * other._z
        return Vector3D(self._x * other, self._y * other, self._z * other)
    
    @not_instance(float)
    def __truediv__(self, scalar: float): 
        """Divide a Vector3D instance by a scalar."""
        if scalar == 0.0:
            raise ValueError("Cannot divide by zero")
        return Vector3D(self._x / scalar, self._y / scalar, self._z / scalar)
    
    @not_self_instance
    def cross(self, other: 'Vector3D') -> 'Vector3D':
        """Compute the cross product of two vectors."""
        return Vector3D(self._y * other._z - self._z * other._y, self._z * other._x - self._x * other._z, self._x * other._y - self._y * other._x)
    
    @not_instance(int)
    def norm(self, p: int = 2) -> float:
        """Compute the norm of the vector."""
        if p <= 0:
            raise ValueError("p must be a positive number")
        return (math.pow(math.fabs(self._x), p) + math.pow(math.fabs(self._y), p) + math.pow(math.fabs(self._z), p)) ** (1/p)