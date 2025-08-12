import pytest
from comgeo.core.vector import Vector2D
from comgeo.core.vertex import Vertex2D

class TestVector2D:
    def test_init_and_repr(self):
        v = Vector2D(1.0, 2.0, id=5, visited=True)
        assert v._x == 1.0
        assert v._y == 2.0
        assert v.id == 5
        assert v.visited is True
        assert repr(v) == "Vector2D(x=1.0, y=2.0, id=5, visited=True)"

    def test_eq(self):
        v1 = Vector2D(1.0, 2.0)
        v2 = Vector2D(1.0, 2.0)
        v3 = Vector2D(2.0, 1.0)
        assert v1 == v2
        assert not (v1 == v3)
        with pytest.raises(NotImplementedError):
            v1 == object()

    def test_lt(self):
        v1 = Vector2D(1.0, 2.0)
        v2 = Vector2D(2.0, 1.0)
        assert v1 < v2
        with pytest.raises(NotImplementedError):
            v1 < object()

    def test_add(self):
        v1 = Vector2D(1.0, 2.0)
        v2 = Vector2D(3.0, 4.0)
        v3 = v1 + v2
        assert isinstance(v3, Vector2D)
        assert v3._x == 4.0 and v3._y == 6.0
        with pytest.raises(NotImplementedError):
            v1 + object()

    def test_sub(self):
        v1 = Vector2D(5.0, 7.0)
        v2 = Vector2D(2.0, 3.0)
        v3 = v1 - v2
        assert isinstance(v3, Vector2D)
        assert v3._x == 3.0 and v3._y == 4.0
        with pytest.raises(NotImplementedError):
            v1 - object()

    def test_from_vertices(self):
        vert1 = Vertex2D(1.0, 2.0)
        vert2 = Vertex2D(4.0, 6.0)
        v = Vector2D.from_vertices(vert1, vert2, id=10)
        assert isinstance(v, Vector2D)
        assert v._x == 3.0 and v._y == 4.0 and v.id == 10

    def test_from_vertice(self):
        vert = Vertex2D(2.5, -1.5)
        v = Vector2D.from_vertice(vert)
        assert isinstance(v, Vector2D)
        assert v._x == 2.5 and v._y == -1.5

    def test_norm(self):
        v = Vector2D(3.0, 4.0)
        assert abs(v.norm() - 5.0) < 1e-8
        v = Vector2D(1.0, 1.0)
        assert abs(v.norm(1) - 2.0) < 1e-8
