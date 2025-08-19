from .base import Polygon
from ..vertex import Vertex, Vertex2D, Vertex3D
from ...decorator.error import not_instance, not_self_implemented
from ...functional.polygon.area import get_area
from ...functional.polygon.point_cloud import point_cloud_sampling_triangle


class Triangle(Polygon):
    def __init__(self, vertices: list[Vertex | Vertex2D | Vertex3D], id: int = -1, visited: bool = False):
        self.check_vertices_len(vertices)
        super().__init__(vertices, id, visited)

        self._area = get_area(vertices)
    
    @staticmethod
    def check_vertices_len(vertices: list[Vertex | Vertex2D | Vertex3D]):
        if len(vertices) != 3:
            raise ValueError("Triangle must have 3 vertices")
    
    @Polygon.vertices.setter
    @not_instance(list)
    def vertices(self, vertices: list[Vertex | Vertex2D | Vertex3D]):
        self.check_vertices_len(vertices)
        super(Triangle, type(self)).vertices.fset(self, vertices)
    
    def __repr__(self):
        return f"Triangle(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"
    
    def __str__(self):
        return f"Triangle(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"
    
    @not_self_implemented
    def is_convex(self) -> bool:
        pass

    def point_cloud_sampling(self, num_points: int) -> list[Vertex | Vertex2D | Vertex3D]:
        if type(self._vertices[0]) not in [Vertex2D, Vertex3D]:
            raise NotImplementedError("point_cloud_sampling not implemented for " + str(type(self._vertices[0])))
        
        points: list[Vertex2D | Vertex3D] = point_cloud_sampling_triangle(self._vertices, num_points)
        return points