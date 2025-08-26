from ...vertex import Vertex, Vertex2D, Vertex3D
from ....functional.vertex.triplets.check import is_ccw
from ....functional.polygon.center import get_center

from ....decorator.error import not_instance, not_self_implemented, not_self_instance
from ...utils.error import check_type, check_consistency

import numpy as np


class Face:
    def __init__(self, vertex_ids: list[int], id: int = -1, visited: bool = False, max_num_vertices: int | None = None):
        check_type(vertex_ids, list, "vertex_ids")
        check_type(id, int, "id")
        check_type(visited, bool, "visited")
        check_type(max_num_vertices, int | None, "max_num_vertices")
        self._vertex_ids = vertex_ids
        self._id = id
        self._visited = visited
        self._center: Vertex2D | Vertex3D | None = None
        self._area: float | None = None 
        self._max_num_vertices = max_num_vertices

        if max_num_vertices is not None:
            assert len(vertex_ids) <= max_num_vertices, "Number of vertices in face exceeds max_num_vertices"
    
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
    def vertex_ids(self):
        return self._vertex_ids
    
    @vertex_ids.setter
    @not_instance(list)
    def vertex_ids(self, vertex_ids: list[int]):
        check_consistency(vertex_ids, "vertex_ids")
        if self._max_num_vertices is not None:
            assert len(vertex_ids) <= self._max_num_vertices, "Number of vertices in face exceeds max_num_vertices"
        self._vertex_ids = vertex_ids
    
    @property
    def center(self, all_vertices: list[Vertex | Vertex2D | Vertex3D]):
        self._center = get_center([all_vertices[i] for i in self._vertex_ids])
        return self._center
    
    @center.setter
    @not_instance(Vertex2D | Vertex3D)
    def center(self, center: Vertex2D | Vertex3D):
        self._center = center
    
    @not_self_implemented
    def area(self, all_vertices: list[Vertex | Vertex2D | Vertex3D]):
        pass
    
    @not_instance(float)
    @not_self_implemented
    def set_area(self, area: float):
        pass

    @not_self_instance
    def __eq__(self, other: 'Face') -> bool:
        return self.id == other.id and self.visited == other.visited and self.vertex_ids == other.vertex_ids
    
    def __repr__(self):
        return f"Face(id={self._id}, visited={self._visited}, \nvertex_ids={self._vertex_ids})"
    
    def __str__(self):
        return f"Face(id={self._id}, visited={self._visited}, \nvertex_ids={self._vertex_ids})"
    
    def __getitem__(self, key: int) -> int:
        return self._vertex_ids[key]
    
    def __setitem__(self, key: int, value: int):
        self._vertex_ids[key] = value

    def is_convex(self, all_vertices: list[Vertex | Vertex2D | Vertex3D]) -> bool:
        vertices = [all_vertices[i] for i in self._vertex_ids]

        if type(vertices[0]) in [Vertex, Vertex3D]:
            raise NotImplementedError("is_convex not implemented for " + str(type(vertices[0])))

        ccws = np.array([
            is_ccw(vertices[i], vertices[(i + 1) % len(vertices)], vertices[(i + 2) % len(vertices)])
            for i in range(len(vertices))
        ])

        print(ccws)

        return np.all(ccws) or not np.any(ccws)

    @not_self_implemented
    def point_cloud_sampling(self, num_points: int, all_vertices: list[Vertex | Vertex2D | Vertex3D]) -> list[Vertex | Vertex2D | Vertex3D]:
        pass