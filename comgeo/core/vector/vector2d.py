from .base import Vector
from ..vertex import Vertex2D

from ...decorator.error import not_self_instance, not_instance

import math

class Vector2D(Vector):
    def __init__(self, x: float, y: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        self._x = x
        self._y = y

    @staticmethod
    def from_vertices(v1: Vertex2D, v2: Vertex2D, id: int, visited: bool = False) -> 'Vector2D':
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

    @not_instance(int)
    def norm(self, p: int = 2) -> float:
        """Compute the norm of the vector."""
        if p <= 0:
            raise ValueError("p must be a positive number")
        return (math.pow(math.fabs(self._x), p) + math.pow(math.fabs(self._y), p)) ** (1/p)