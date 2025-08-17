from ..vertex import Vertex, Vertex2D, Vertex3D
from .base import Polygon
from ...decorator.error import not_instance, not_self_implemented

from random import random
import math

class Triangle(Polygon):
    def __init__(self, vertices: list[Vertex | Vertex2D | Vertex3D], id: int = -1, visited: bool = False):
        self.check_vertices_len(vertices)
        super().__init__(vertices, id, visited)
    
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
        
        points: list[Vertex2D | Vertex3D] = []
        for _ in range(num_points):
            r1 = random()
            r2 = random()

            w1 = 1 - math.sqrt(r1)
            w2 = math.sqrt(r1) * (1 - r2)
            w3 = math.sqrt(r1) * r2

            points.append(
                self.vertices[0] * w1 + \
                self.vertices[1] * w2 + \
                self.vertices[2] * w3
            )
        
        return points