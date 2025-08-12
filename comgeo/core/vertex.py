import math

class Vertex:
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
        return f"Vertex(id={self._id}, visited={self._visited})"

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            raise NotImplementedError("Comparison is only supported between Vertex instances.")
        return self._id == other._id

    def __lt__(self, other: 'Vertex'):
        raise NotImplementedError("< is not supported for core Vertex instances.")

    def __add__(self, other: 'Vertex'):
        raise NotImplementedError("Addition is not supported for core Vertex instances.")

    def __sub__(self, other: 'Vertex'):
        raise NotImplementedError("Subtraction is not supported for core Vertex instances.")

class Vertex2D(Vertex):
    def __init__(self, x: float, y: float, id: int = -1, visited: bool = False):
        super().__init__(id, visited)
        self._x = x
        self._y = y

    @property
    def coordinates(self):
        return self._x, self._y
    
    def set_coordinates(self, x: float, y: float):
        self._x = x
        self._y = y

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

    def __repr__(self):
        return f"Vertex2D(x={self._x}, y={self._y}, id={self._id}, visited={self._visited})"

    def __eq__(self, other: 'Vertex2D') -> bool:
        if not isinstance(other, Vertex2D):
            raise NotImplementedError("Comparison is only supported between Vertex2D instances.")
        return self._x == other._x and self._y == other._y

    def __lt__(self, other: 'Vertex2D') -> bool:
        if not isinstance(other, Vertex2D):
            raise NotImplementedError("Comparison is only supported between Vertex2D instances.")
        return (self._x, self._y) < (other._x, other._y)

    def __add__(self, other: 'Vertex2D') -> 'Vertex2D':
        if not isinstance(other, Vertex2D):
            raise NotImplementedError("Addition is not supported for Vertex2D instances.")
        return Vertex2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other: 'Vertex2D') -> 'Vertex2D':
        if not isinstance(other, Vertex2D):
            raise NotImplementedError("Subtraction is not supported for Vertex2D instances.")
        return Vertex2D(self._x - other._x, self._y - other._y)

    def distance_to(self, other: 'Vertex2D') -> float:
        if not isinstance(other, Vertex2D):
            raise NotImplementedError("Distance calculation is only supported between Vertex2D instances.")
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5
