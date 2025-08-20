from ...vertex import Vertex, Vertex2D, Vertex3D
from ....functional.polygon.area import get_area
from ....decorator.error import not_instance, not_self_implemented
from ....functional.polygon.point_cloud import point_cloud_sampling_triangle

from .face import Face


class TriangleFace(Face):
    def __init__(self, vertex_ids: list[int], id: int = -1, visited: bool = False):
        super().__init__(vertex_ids, id, visited, 3)
    
    def area(self, all_vertices: list[Vertex | Vertex2D | Vertex3D]):
        if self._area is None:
            self._area = get_area([all_vertices[i] for i in self._vertex_ids])
        return self._area
    
    @not_instance(float)
    def set_area(self, area: float):
        self._area = area
    
    @not_self_implemented
    def is_convex(self, all_vertices: list[Vertex | Vertex2D | Vertex3D]) -> bool:
        pass
    
    def point_cloud_sampling(self, num_points: int, all_vertices: list[Vertex | Vertex2D | Vertex3D]) -> list[Vertex | Vertex2D | Vertex3D]:
        return point_cloud_sampling_triangle([all_vertices[i] for i in self._vertex_ids], num_points)