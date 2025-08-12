import pytest
from comgeo.core.vertex import Vertex2D

class TestVertex2D:
    def test_init_and_repr(self):
        v = Vertex2D(1.0, 2.0, id=5, visited=True)
        assert v._x == 1.0
        assert v._y == 2.0
        assert v.id == 5
        assert v.visited is True
        assert repr(v) == "Vertex2D(x=1.0, y=2.0, id=5, visited=True)"

    def test_set_coordinates(self):
        v = Vertex2D(0.0, 0.0)
        v.set_coordinates(3.5, -2.1)
        assert v._x == 3.5
        assert v._y == -2.1

    def test_equality(self):
        v1 = Vertex2D(1.0, 2.0)
        v2 = Vertex2D(1.0, 2.0)
        v3 = Vertex2D(2.0, 1.0)
        assert v1 == v2
        assert not (v1 == v3)
        with pytest.raises(NotImplementedError):
            v1 == object()

    def test_lt(self):
        v1 = Vertex2D(1.0, 2.0)
        v2 = Vertex2D(2.0, 1.0)
        assert v1 < v2
        with pytest.raises(NotImplementedError):
            v1 < object()

    def test_add(self):
        v1 = Vertex2D(1.0, 2.0)
        v2 = Vertex2D(3.0, 4.0)
        v3 = v1 + v2
        assert isinstance(v3, Vertex2D)
        assert v3.x == 4.0 and v3.y == 6.0
        with pytest.raises(NotImplementedError):
            v1 + object()

    def test_sub(self):
        v1 = Vertex2D(5.0, 7.0)
        v2 = Vertex2D(2.0, 3.0)
        v3 = v1 - v2
        assert isinstance(v3, Vertex2D)
        assert v3.x == 3.0 and v3.y == 4.0
        with pytest.raises(NotImplementedError):
            v1 - object()

    def test_distance_to(self):
        v1 = Vertex2D(0.0, 0.0)
        v2 = Vertex2D(3.0, 4.0)
        assert v1.distance_to(v2) == 5.0
        with pytest.raises(NotImplementedError):
            v1.distance_to(object())
