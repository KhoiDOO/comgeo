from ...decorator.error import not_self_implemented, not_self_instance, not_instance
from ..utils.error import check_type

class Vector:
    def __init__(self, id: int = -1, visited: bool = False):
        check_type(id, int, "id")
        check_type(visited, bool, "visited")
        self._id = id
        self._visited = visited

    @property
    def id(self):
        return self._id

    @id.setter
    @not_instance(int)
    def id(self, value: int):
        self._id = value

    @property
    def visited(self):
        return self._visited

    @visited.setter
    @not_instance(bool)
    def visited(self, value: bool):
        self._visited = value

    def __repr__(self):
        return f"Vector(id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other):
        """Check equality based on the id of the vector."""
        return self._id == other._id

    @not_self_implemented
    def __lt__(self, other: 'Vector'):
        """Less than comparison based on the id of the vector."""
        pass

    @not_self_implemented
    def __add__(self, other: 'Vector'):
        """Addition operation for vectors."""
        pass
    
    @not_self_implemented
    def __sub__(self, other: 'Vector'):
        """Subtraction operation for vectors."""
        pass

    @not_self_implemented
    def norm(self, p: int = 2) -> float:
        """Compute the norm of the vector."""
        pass

    @not_self_implemented
    def __mul__(self, scalar: float): 
        """Multiply a Vector instance by a scalar."""
        pass

    @not_self_implemented
    def __truediv__(self, scalar: float): 
        """Divide a Vector instance by a scalar."""
        pass