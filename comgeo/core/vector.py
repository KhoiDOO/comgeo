import math

from .vertex import Vertex2D

class Vector:
    def __init__(self, id: int = -1, visited: bool = False):
        self._id = id
        self._visited = visited

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value: bool):
        self._visited = value

    def __repr__(self):
        return f"Vector(id={self._id}, visited={self._visited})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Comparison is only supported between Vector instances.")
        return self._id == other._id

    def __lt__(self, other: 'Vector'):
        raise NotImplementedError("< is not supported for core Vector instances.")

    def __add__(self, other: 'Vector'):
        raise NotImplementedError("Addition is not supported for core Vector instances.")

    def __sub__(self, other: 'Vector'):
        raise NotImplementedError("Subtraction is not supported for core Vector instances.")

class Vector2D(Vector):
    def __init__(self, x: float, y: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        self._x = x
        self._y = y

    @staticmethod
    def from_vertices(v1: Vertex2D, v2: Vertex2D, id: int, visited: bool = False) -> 'Vector2D':
        return Vector2D(x=v2.x - v1.x, y=v2.y - v1.y, id=id, visited=visited)

    @staticmethod
    def from_vertice(v: Vertex2D) -> 'Vector2D':
        return Vector2D(x=v.x, y=v.y)

    def __repr__(self):
        return f"Vector2D(x={self._x}, y={self._y}, id={self._id}, visited={self._visited})"

    def __eq__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            raise NotImplementedError("Comparison is only supported between Vector2D instances.")
        return self._x == other._x and self._y == other._y

    def __lt__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            raise NotImplementedError("Comparison is only supported between Vector2D instances.")
        return (self._x, self._y) < (other._x, other._y)

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        if not isinstance(other, Vector2D):
            raise NotImplementedError("Addition is not supported for Vector2D instances.")
        return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        if not isinstance(other, Vector2D):
            raise NotImplementedError("Subtraction is not supported for Vector2D instances.")
        return Vector2D(self._x - other._x, self._y - other._y)

    def norm(self, p: int = 2) -> float:
        return (math.pow(math.fabs(self._x), p) + math.pow(math.fabs(self._y), p)) ** (1/p)