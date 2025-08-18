from ...core.vertex import Vertex2D, Vertex3D
from ...core.utils.error import check_type, check_consistency

def get_center(vertices: list[Vertex2D | Vertex3D]) -> Vertex2D | Vertex3D:
    check_type(vertices, list, "vertices")
    check_consistency(vertices, "vertices")
    if type(vertices[0]) not in [Vertex2D, Vertex3D]:
        raise ValueError("Polygon must have vertices of type Vertex2D or Vertex3D")
    
    sum_vertex: Vertex2D | Vertex3D = Vertex2D(0.0, 0.0) if type(vertices[0]) == Vertex2D else Vertex3D(0.0, 0.0, 0.0)
    for vertex in vertices:
        sum_vertex += vertex
    return sum_vertex / float(len(vertices))