from .base import Vector
from ..vertex import Vertex3D

from ...decorator.error import not_self_instance, not_instance

import math

class Vector3D(Vector):
    def __init__(self, x: float, y: float, z: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)

        self._x = x
        self._y = y
        self._z = z

    @staticmethod
    def from_vertices(v1: Vertex3D, v2: Vertex3D, id: int, visited: bool = False) -> 'Vector3D':
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

    @not_instance(int)
    def norm(self, p: int = 2) -> float:
        """Compute the norm of the vector."""
        if p <= 0:
            raise ValueError("p must be a positive number")
        return (math.pow(math.fabs(self._x), p) + math.pow(math.fabs(self._y), p) + math.pow(math.fabs(self._z), p)) ** (1/p)