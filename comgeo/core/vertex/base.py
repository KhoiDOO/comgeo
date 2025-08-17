from ...decorator.error import not_instance, not_self_implemented, not_self_instance
from ..utils.error import check_type

class Vertex:
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
        return f"Vertex(id={self._id}, visited={self._visited})"

    @not_self_instance
    def __eq__(self, other):
        """Check equality of Vertex instances based on their IDs."""
        return self._id == other._id

    @not_self_implemented
    def __lt__(self, other: 'Vertex'): 
        """Compare Vertex instances based on their IDs."""
        pass

    @not_self_implemented
    def __add__(self, other: 'Vertex'): 
        """Add two Vertex instances."""
        pass

    @not_self_implemented
    def __sub__(self, other: 'Vertex'): 
        """Subtract two Vertex instances."""
        pass

    @not_self_implemented
    def __mul__(self, scalar: float): 
        """Multiply a Vertex instance by a scalar."""
        pass

    @not_self_implemented
    def __truediv__(self, scalar: float): 
        """Divide a Vertex instance by a scalar."""
        pass

    @not_self_implemented
    def distance_to(self, other: 'Vertex') -> float:
        """Calculate the Euclidean distance between two Vertex instances."""
        pass