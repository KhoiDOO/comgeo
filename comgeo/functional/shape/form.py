from ...core.vertex import Vertex2D, Vertex3D
from ...core.utils.error import check_type, check_consistency
from ...core.polygon.triangle import Triangle
from ...core.mesh.triangle_mesh import TriangleMesh
from ...core.shape.circle import Circle


def circumcircle_vertices(vertices: tuple[Vertex2D, Vertex2D, Vertex2D]) -> Circle:

    check_consistency(vertices, "vertices")
    check_type(vertices[0], Vertex2D, "vertices[0]")

    A = vertices[0]
    B = vertices[1]
    C = vertices[2]

    D = 2 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y))
    if D == 0:
        raise ValueError("The points are collinear")

    Ux = ((A.x**2 + A.y**2) * (B.y - C.y) + (B.x**2 + B.y**2) * (C.y - A.y) + (C.x**2 + C.y**2) * (A.y - B.y)) / D
    Uy = ((A.x**2 + A.y**2) * (C.x - B.x) + (B.x**2 + B.y**2) * (A.x - C.x) + (C.x**2 + C.y**2) * (B.x - A.x)) / D

    center = Vertex2D(Ux, Uy)
    radius = center.distance_to(A)

    return Circle(center, radius)

def circumcircle_triangle(triangle: Triangle) -> Circle:

    check_type(triangle, Triangle, "triangle")

    return circumcircle_vertices(triangle.vertices)

def circumcircle_triangle_mesh(mesh: TriangleMesh) -> Circle:

    check_type(mesh, TriangleMesh, "mesh")

    return circumcircle_vertices(mesh.vertices)