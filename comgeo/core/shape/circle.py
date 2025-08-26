from .ellipse import Ellipse
from ..vertex import Vertex2D

class Circle(Ellipse):
    def __init__(self, center: Vertex2D, radius: float):
        super().__init__(center, radius, radius)

    @property
    def center(self) -> Vertex2D:
        return self._center

    @property
    def radius(self) -> float:
        return self._rx

    def area(self) -> float:
        return super().area()

    def perimeter(self) -> float:
        return super().perimeter()

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"