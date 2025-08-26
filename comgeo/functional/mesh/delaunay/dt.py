from ....core.vertex import Vertex2D, Vertex3D
from ....core.utils.error import check_type, check_consistency
from ....core.mesh.triangle_mesh import TriangleMesh2D
from ....core.shape.circle import Circle
from ....functional.shape.form import circumcircle_vertices
from ....core.mesh.edges.base import BaseEdge2D

from tqdm import tqdm


def is_delaunay(triangle: tuple[Vertex2D | Vertex3D, Vertex2D | Vertex3D, Vertex2D | Vertex3D], vertices: list[Vertex2D | Vertex3D]) -> bool:
    # Placeholder for actual Delaunay condition check
    try:
        cc: Circle = circumcircle_vertices(triangle)
    except Exception as e:
        return False

    for v in vertices:
        if v not in triangle and cc.contains(v):
            return False
    return True


def delaunay_triangulation_naive(vertices: list[Vertex2D], verbose: bool = False, progress_bar: bool = False, refine: bool = False) -> TriangleMesh2D:
    check_type(vertices, list, "vertices")
    check_consistency(vertices, "vertices")
    if len(vertices) == 0:
        raise ValueError("Vertex list is empty")

    triangles: list[list[Vertex2D | Vertex3D, Vertex2D | Vertex3D, Vertex2D | Vertex3D]] = []
    edges: list[BaseEdge2D] = []
    bad_edges: list[BaseEdge2D] = []

    for idx, vertice in enumerate(vertices):
        vertice.id = idx

    if verbose:
        print("Start constructing base list of triangles")

    for v1 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
        for v2 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
            for v3 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
                if v1 != v2 and v2 != v3 and v1 != v3:
                    if is_delaunay((v1, v2, v3), vertices):
                        triangles.append((v1, v2, v3))
    if verbose:
        print(f"Constructed {len(triangles)} initial triangles")

    if refine:

        if verbose:
            print("Start constructing base list of edges")

        for triangle in tqdm(triangles, desc="Processing Triangles") if progress_bar else triangles:
            if not is_delaunay(triangle, vertices):
                triangles.remove(triangle)
            else:
                edges.append(BaseEdge2D(triangle[0], triangle[1]))
                edges.append(BaseEdge2D(triangle[1], triangle[2]))
                edges.append(BaseEdge2D(triangle[2], triangle[0]))

        if verbose:
            print(f"Constructed {len(edges)} initial edges")
            print("Start checking for bad edges")

        for e1 in tqdm(edges, desc="Processing Edges") if progress_bar else edges:
            for e2 in tqdm(edges, desc="Processing Edges") if progress_bar else edges:
                if e1 != e2 and e1.intersect(e2):
                    len_e1 = e1.length()
                    len_e2 = e2.length()
                    if len_e1 >= len_e2:
                        bad_edges.append(e1)
                    else:
                        bad_edges.append(e2)

        for bad_edge in tqdm(bad_edges, desc="Processing Bad Edges") if progress_bar else bad_edges:
            for edge in tqdm(edges, desc="Processing Edges") if progress_bar else edges:
                if bad_edge == edge:
                    edges.remove(bad_edge)

        if verbose:
            print(f"Removed {len(bad_edges)} bad edges")
            print("Start constructing final list of triangles")
        
        triangles_ids: list[list[int, int, int]] = []
        edge_tuples = [(e.start, e.end) for e in edges]
        for v1 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
            for v2 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
                for v3 in tqdm(vertices, desc="Processing Vertices") if progress_bar else vertices:
                    if v1 != v2 and v2 != v3 and v1 != v3:
                        if ((v1, v2) in edge_tuples or (v2, v1) in edge_tuples) and \
                        ((v2, v3) in edge_tuples or (v3, v2) in edge_tuples) and \
                        ((v3, v1) in edge_tuples or (v1, v3) in edge_tuples):
                            triangles_ids.append([v1.id, v2.id, v3.id])

    else:
        triangles_ids: list[list[int, int, int]] = [
            [v1.id, v2.id, v3.id] for v1, v2, v3 in triangles
        ]

    return TriangleMesh2D(vertices, triangles_ids)