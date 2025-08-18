from .base import Polygon
from ..vertex import Vertex, Vertex2D, Vertex3D
from ...decorator.error import not_instance
from ...functional.polygon.area import get_area

from random import random

class Quad(Polygon):
    """A quadrilateral, a polygon with 4 vertices."""

    def __init__(self, vertices: list[Vertex | Vertex2D | Vertex3D], id: int = -1, visited: bool = False):
        self.check_vertices_len(vertices)
        super().__init__(vertices, id, visited)

        self._area = get_area(vertices)

    @staticmethod
    def check_vertices_len(vertices: list[Vertex | Vertex2D | Vertex3D]):
        """Check if the number of vertices is 4."""
        if len(vertices) != 4:
            raise ValueError("Quad must have 4 vertices")

    @Polygon.vertices.setter
    @not_instance(list)
    def vertices(self, vertices: list[Vertex | Vertex2D | Vertex3D]):
        """Set the vertices of the quad."""
        self.check_vertices_len(vertices)
        super(Quad, type(self)).vertices.fset(self, vertices)

    def __repr__(self):
        return f"Quad(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"

    def __str__(self):
        return f"Quad(id={self._id}, visited={self._visited}, \nvertices={self._vertices})"

    def is_convex(self) -> bool:
        return super().is_convex()

    def point_cloud_sampling(self, num_points: int) -> list[Vertex | Vertex2D | Vertex3D]:
        if type(self._vertices[0]) not in [Vertex2D, Vertex3D]:
            raise NotImplementedError("point_cloud_sampling not implemented for " + str(type(self._vertices[0])))

        points: list[Vertex2D | Vertex3D] = []
        for _ in range(num_points):
            l = random()
            r = random()

            a1 = (1 - l) * (1 - r)
            a2 = l * (1 - r)
            a3 = l * r
            a4 = (1 - l) * r

            points.append(
                self.vertices[0] * a1 + \
                self.vertices[1] * a2 + \
                self.vertices[2] * a3 + \
                self.vertices[3] * a4
            )
        
        return points
        