from ..vertex import Vertex, Vertex2D, Vertex3D
from ...functional.vertex.triplets.check import is_ccw

from ...decorator.error import not_instance, not_self_implemented
from ..utils.error import check_type, check_consistency

class Polygon:
    def __init__(self, vertices: list[Vertex | Vertex2D | Vertex3D], id: int = -1, visited: bool = False):
        check_type(vertices, list, "vertices")
        check_consistency(vertices, "vertices")
        check_type(id, int, "id")
        check_type(visited, bool, "visited")
        
        self._vertices = vertices
        self._id = id
        self._visited = visited
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    @not_instance(int)
    def id(self, id: int):
        self._id = id
    
    @property
    def visited(self):
        return self._visited
    
    @visited.setter
    @not_instance(bool)
    def visited(self, visited: bool):
        self._visited = visited
    
    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    @not_instance(list)
    def vertices(self, vertices: list[Vertex | Vertex2D | Vertex3D]):
        check_consistency(vertices, "vertices")
        self._vertices = vertices
    
    def __eq__(self, other):
        if not isinstance(other, Polygon):
            return NotImplemented
        return self.id == other.id and self.visited == other.visited and self.vertices == other.vertices

    def __repr__(self):
        return f"Polygon(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"
    
    def __str__(self):
        return f"Polygon(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"
    
    def is_convex(self) -> bool:
        if type(self._vertices[0]) in [Vertex, Vertex3D]:
            raise NotImplementedError("is_convex not implemented for " + str(type(self._vertices[0])))
        
        for i in range(len(self._vertices)):
            if not is_ccw(self._vertices[i], self._vertices[(i + 1) % len(self._vertices)], self._vertices[(i + 2) % len(self._vertices)]):
                return False
        return True
    
    @not_self_implemented
    def point_cloud_sampling(self, num_points: int) -> list[Vertex | Vertex2D | Vertex3D]:
        pass