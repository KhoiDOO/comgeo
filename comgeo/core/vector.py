import math

from .vertex import Vertex2D, Vertex3D

from ..decorator.error import not_implemented, not_self_instance, not_instance

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

    @not_self_instance
    def __eq__(self, other):
        """Check equality based on the id of the vector."""
        return self._id == other._id

    @not_implemented
    def __lt__(self, other: 'Vector'):
        """Less than comparison based on the id of the vector."""
        pass

    @not_implemented
    def __add__(self, other: 'Vector'):
        """Addition operation for vectors."""
        pass
    
    @not_implemented
    def __sub__(self, other: 'Vector'):
        """Subtraction operation for vectors."""
        pass

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