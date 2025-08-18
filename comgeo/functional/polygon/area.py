from ...core.vertex import Vertex2D, Vertex3D
from ...core.vector import Vector2D, Vector3D
from ...core.utils.error import check_type, check_consistency

def get_triangle_area_2d(vertices: list[Vertex2D]) -> float:
    side_vector_0: Vector2D = Vector2D.from_vertices(vertices[0], vertices[1])
    side_vector_1: Vector2D = Vector2D.from_vertices(vertices[0], vertices[2])
    cross_vector: float = side_vector_0.cross(side_vector_1)
    return cross_vector / 2.0

def get_triangle_area_3d(vertices: list[Vertex3D]) -> float:
    side_vector_0: Vector3D = Vector3D.from_vertices(vertices[0], vertices[1])
    side_vector_1: Vector3D = Vector3D.from_vertices(vertices[0], vertices[2])
    cross_vector: Vector3D = side_vector_0.cross(side_vector_1)
    return cross_vector.norm() / 2.0

def get_triangle_area(vertices: list[Vertex2D | Vertex3D]) -> float:
    if len(vertices) != 3:
        raise ValueError("Triangle must have 3 vertices")
    
    if type(vertices[0]) not in [Vertex2D, Vertex3D]:
        raise ValueError("Triangle must have vertices of type Vertex2D or Vertex3D")
    
    if type(vertices[0]) == Vertex2D:
        return get_triangle_area_2d(vertices)
    else:
        return get_triangle_area_3d(vertices)

def get_quadrilateral_area_2d(vertices: list[Vertex2D]) -> float:
    # Split quadrilateral into two triangles and sum their areas
    # Triangle 1: 0, 1, 2
    area1 = get_triangle_area_2d([vertices[0], vertices[1], vertices[2]])
    # Triangle 2: 0, 2, 3
    area2 = get_triangle_area_2d([vertices[0], vertices[2], vertices[3]])
    return area1 + area2

def get_quadrilateral_area_3d(vertices: list[Vertex3D]) -> float:
    # Split quadrilateral into two triangles and sum their areas
    # Triangle 1: 0, 1, 2
    area1 = get_triangle_area_3d([vertices[0], vertices[1], vertices[2]])
    # Triangle 2: 0, 2, 3
    area2 = get_triangle_area_3d([vertices[0], vertices[2], vertices[3]])
    return area1 + area2

def get_quadrilateral_area(vertices: list[Vertex2D | Vertex3D]) -> float:
    if len(vertices) != 4:
        raise ValueError("Quadrilateral must have 4 vertices")
    
    if type(vertices[0]) not in [Vertex2D, Vertex3D]:
        raise ValueError("Quadrilateral must have vertices of type Vertex2D or Vertex3D")
    
    if type(vertices[0]) == Vertex2D:
        return get_quadrilateral_area_2d(vertices)
    else:
        return get_quadrilateral_area_3d(vertices)

def get_area(vertices: list[Vertex2D | Vertex3D]) -> float:
    check_type(vertices, list, "vertices")
    check_consistency(vertices, "vertices")
    check_type(vertices[0], (Vertex2D, Vertex3D), "vertices")
    if len(vertices) < 3:
        raise ValueError("Polygon must have at least 3 vertices")
    if len(vertices) > 4:
        raise ValueError("Polygon must have at most 4 vertices")
    if len(vertices) == 3:
        return get_triangle_area(vertices)
    if len(vertices) == 4:
        return get_quadrilateral_area(vertices)