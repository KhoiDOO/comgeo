from ....core.vertex import Vertex2D, Vertex3D
from .obj import read_obj

import os

def load_mesh(file_path: str, dim: int = 2, verbose: bool = False) -> tuple[list[Vertex2D | Vertex3D], list[list[int]]]:

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = file_path.split('.')[-1]
    if extension == 'obj':
        _vertices, _vertices_normal, faces = read_obj(file_path, verbose)
        vertices = []

        vertex_id = 0

        if dim == 2:
            for v in _vertices:
                if len(v) != 2:
                    raise Warning(f"Identified vertex with {len(v)} coordinates: {v}, skip it")
                    continue
                vertex = Vertex2D(v[0], v[1], vertex_id)
                vertices.append(vertex)
                vertex_id += 1

        elif dim == 3:
            # for v, vn in zip(_vertices, _vertices_normal):
            #     if len(v) != 3:
            #         raise Warning(f"Identified vertex with {len(v)} coordinates, skip it")
            #         continue
            #     vertex = Vertex3D(v[0], v[1], v[2], vertex_id)
            #     vertex.normal = vn
            #     vertices.append(vertex)
            #     vertex_id += 1

            for v in _vertices:
                if len(v) != 3:
                    raise Warning(f"Identified vertex with {len(v)} coordinates: {v}, skip it")
                    continue
                vertex = Vertex3D(v[0], v[1], v[2], vertex_id)
                vertices.append(vertex)
                vertex_id += 1
        
        return vertices, faces