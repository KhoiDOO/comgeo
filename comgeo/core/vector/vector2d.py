from .base import Vector
from ..vertex import Vertex2D

from ...decorator.error import not_self_instance, not_instance
from ..utils.error import check_type

import math

class Vector2D(Vector):
    def __init__(self, x: float, y: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        check_type(x, float, "x")
        check_type(y, float, "y")
        self._x = x
        self._y = y
    
    @property
    def coordinates(self):
        return self._x, self._y
    
    def set_coordinates(self, x: float, y: float):
        check_type(x, float, "x")
        check_type(y, float, "y")
        self._x = x
        self._y = y
    
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

    @staticmethod
    def from_vertices(v1: Vertex2D, v2: Vertex2D, id: int = -1, visited: bool = False) -> 'Vector2D':
        """Create a Vector2D from two Vertex2D instances."""
        if not isinstance(v1, Vertex2D) or not isinstance(v2, Vertex2D):
            raise TypeError("Both arguments must be Vertex2D instances.")
        return Vector2D(x=v2.x - v1.x, y=v2.y - v1.y, id=id, visited=visited)

    @staticmethod
    @not_instance(Vertex2D)
    def from_vertex(v: Vertex2D) -> 'Vector2D':
        """Create a Vector2D from a Vertex2D instance."""
        return Vector2D(x=v.x, y=v.y)

    def __repr__(self):
        return f"Vector2D(x={self._x}, y={self._y}, id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other: 'Vector2D') -> bool:
        """Check equality based on the coordinates of the vector."""
        return self._x == other._x and self._y == other._y

    @not_self_instance
    def __lt__(self, other: 'Vector2D') -> bool:
        """Check if this vector is less than another vector."""
        return (self._x, self._y) < (other._x, other._y)

    @not_self_instance
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """Add two vectors."""
        return Vector2D(self._x + other._x, self._y + other._y)

    @not_self_instance
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """Subtract two vectors."""
        return Vector2D(self._x - other._x, self._y - other._y)
    
    def __mul__(self, other) -> 'Vector2D': 
        """Multiply a Vector2D instance by a scalar or another Vector2D."""
        if not isinstance(other, (float, Vector2D)):
            raise TypeError("Other must be a float or Vector2D instance")
        if isinstance(other, Vector2D):
            return (self._x * other._x + self._y * other._y)
        return Vector2D(self._x * other, self._y * other)
    
    @not_instance(float)
    def __truediv__(self, other: float) -> 'Vector2D': 
        """Divide a Vector2D instance by a scalar."""
        if other == 0.0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self._x / other, self._y / other)
    
    @not_self_instance
    def cross(self, other: 'Vector2D') -> float:
        """Compute the cross product of two vectors."""
        return self._x * other._y - self._y * other._x
    
    @not_instance(int)
    def norm(self, p: int = 2) -> float:
        """Compute the norm of the vector."""
        if p <= 0:
            raise ValueError("p must be a positive number")
        return (math.pow(abs(self._x), p) + math.pow(abs(self._y), p)) ** (1/p)