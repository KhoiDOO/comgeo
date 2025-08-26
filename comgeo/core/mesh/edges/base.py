from ...vertex import Vertex2D, Vertex3D
from ...vector import Vector2D, Vector3D
from ....decorator.error import not_instance, not_self_implemented
from ...utils.error import check_type, check_consistency
from ....functional.vertex.triplets.check import is_ccw


class BaseEdge:
    def __init__(self, start: Vertex2D, end: Vertex2D):
        check_type(start, (Vertex2D, Vector3D), "start")
        check_type(end, (Vertex2D, Vector3D), "end")
        check_consistency([start, end], "<Vector2D, Vector3D>")
        self._start = start
        self._end = end
    
    @property
    def start(self) -> Vertex2D:
        return self._start

    @property
    def end(self) -> Vertex2D:
        return self._end

    def length(self) -> float:
        return self._start.distance_to(self._end)

    def __repr__(self):
        return f"BaseEdge(start={self._start}, end={self._end})"

    def __str__(self):
        return str([[self._start.x, self._start.y], [self._end.x, self._end.y]])

    def intersect(self, other: 'BaseEdge') -> bool:
        check_type(other, BaseEdge, "other")

        v1 = self._start
        v2 = self._end
        v3 = other.start
        v4 = other.end

        return (is_ccw(v1, v3, v4) != is_ccw(v2, v3, v4)) \
            and (is_ccw(v1, v2, v3) != is_ccw(v1, v2, v4))

class BaseEdge2D(BaseEdge):
    def __init__(self, start: Vertex2D, end: Vertex2D):
        check_type(start, Vertex2D, "start")
        check_type(end, Vertex2D, "end")
        super().__init__(start, end)

class BaseEdge3D(BaseEdge):
    def __init__(self, start: Vertex3D, end: Vertex3D):
        check_type(start, Vertex3D, "start")
        check_type(end, Vertex3D, "end")
        super().__init__(start, end)
