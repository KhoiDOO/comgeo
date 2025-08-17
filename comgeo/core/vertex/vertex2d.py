from .base import Vertex
from ...decorator.error import not_instance, not_self_instance
from ..utils.error import check_type

class Vertex2D(Vertex):
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

    def __repr__(self):
        return f"Vertex2D(x={self._x}, y={self._y}, id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other: 'Vertex2D') -> bool:
        """Check equality of Vertex2D instances based on their coordinates."""
        return self._x == other._x and self._y == other._y

    @not_self_instance
    def __lt__(self, other: 'Vertex2D') -> bool:
        """Compare Vertex2D instances based on their coordinates."""
        return (self._x, self._y) < (other._x, other._y)

    @not_self_instance
    def __add__(self, other: 'Vertex2D') -> 'Vertex2D':
        """Add two Vertex2D instances."""
        return Vertex2D(self._x + other._x, self._y + other._y)

    @not_self_instance
    def __sub__(self, other: 'Vertex2D') -> 'Vertex2D':
        """Subtract two Vertex2D instances."""
        return Vertex2D(self._x - other._x, self._y - other._y)
    
    @not_instance(float)
    def __mul__(self, scalar: float) -> 'Vertex2D':
        """Multiply a Vertex2D instance by a scalar."""
        return Vertex2D(self._x * scalar, self._y * scalar)
    
    @not_instance(float)
    def __truediv__(self, scalar: float) -> 'Vertex2D':
        """Divide a Vertex2D instance by a scalar."""
        if scalar == 0.0:
            raise ValueError("Cannot divide by zero")
        return Vertex2D(self._x / scalar, self._y / scalar)
    
    @not_self_instance
    def distance_to(self, other: 'Vertex2D') -> float:
        """Calculate the Euclidean distance between two Vertex2D instances."""
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5