from .base import Vertex
from ...decorator.error import not_self_instance


class Vertex3D(Vertex):
    def __init__(self, x: float, y: float, z: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        self._x = x
        self._y = y
        self._z = z

    @property
    def coordinates(self):
        return self._x, self._y, self._z
    
    def set_coordinates(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = value

    def __repr__(self):
        return f"Vertex3D(x={self._x}, y={self._y}, z={self._z}, id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other: 'Vertex3D') -> bool:
        """Check equality of Vertex3D instances based on their coordinates."""
        return (self._x == other._x and self._y == other._y and self._z == other._z)

    @not_self_instance
    def __lt__(self, other: 'Vertex3D') -> bool:
        """Compare Vertex3D instances based on their coordinates."""
        return (self._x, self._y, self._z) < (other._x, other._y, other._z)

    @not_self_instance
    def __add__(self, other: 'Vertex3D') -> 'Vertex3D':
        """Add two Vertex3D instances."""
        return Vertex3D(self._x + other._x, self._y + other._y, self._z + other._z)

    @not_self_instance
    def __sub__(self, other: 'Vertex3D') -> 'Vertex3D':
        """Subtract two Vertex3D instances."""
        return Vertex3D(self._x - other._x, self._y - other._y, self._z - other._z)

    @not_self_instance
    def distance_to(self, other: 'Vertex3D') -> float:
        """Calculate the Euclidean distance between two Vertex3D instances."""
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2 + (self._z - other._z) ** 2) ** 0.5