from ...decorator.error import not_self_implemented, not_self_instance

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