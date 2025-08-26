from ..vertex import Vertex2D
from ..utils.error import check_type

import math

class Ellipse:
    def __init__(self, center: Vertex2D, rx: float, ry: float):
        check_type(center, Vertex2D, "center")
        check_type(rx, float, "rx")
        check_type(ry, float, "ry")
        self._center = center
        self._rx = rx
        self._ry = ry

    @property
    def center(self) -> Vertex2D:
        return self._center

    @property
    def rx(self) -> float:
        return self._rx

    @property
    def ry(self) -> float:
        return self._ry

    def area(self) -> float:
        return math.pi * self._rx * self._ry

    def perimeter(self) -> float:
        # Approximation using Ramanujan's formula
        return 2 * math.pi * math.sqrt((self._rx**2 + self._ry**2) / 2)

    def __repr__(self):
        return f"Ellipse(center={self._center}, rx={self._rx}, ry={self._ry})"

    def contains(self, point: Vertex2D) -> bool:
        # Check if a point is inside the ellipse
        dx = point.x - self._center.x
        dy = point.y - self._center.y
        return (dx**2) / (self._rx**2) + (dy**2) / (self._ry**2) <= 1