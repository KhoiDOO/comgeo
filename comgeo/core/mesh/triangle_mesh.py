from ..vertex import Vertex2D, Vertex3D
from .basic import BasicMesh
from .primitives.triangle_face import TriangleFace

from ...functional.mesh.io.load import load_mesh


class TriangleMesh(BasicMesh):
    def __init__(self, 
                 vertices, 
                 faces, 
                 id = -1, 
                 visited = False, 
                 dim = 2
                 ):
        super().__init__(
            vertices = vertices, 
            faces = faces, 
            id = id, 
            visited = visited, 
            face_type = TriangleFace, 
            dim = dim
        )
    
    @staticmethod
    def from_file_path(file_path: str, dim: int = 2) -> "TriangleMesh":
        vertices, faces = load_mesh(file_path, dim)
        return TriangleMesh(
            vertices=vertices,
            faces=faces,
            dim=dim
        )

class TriangleMesh2D(TriangleMesh):
    def __init__(self, 
                 vertices, 
                 faces, 
                 id = -1, 
                 visited = False
                 ):
        super().__init__(
            vertices = vertices, 
            faces = faces, 
            id = id, 
            visited = visited, 
            dim = 2
        )
    
    @staticmethod
    def from_file_path(file_path: str) -> "TriangleMesh2D":
        vertices, faces = load_mesh(file_path, dim=2)
        return TriangleMesh2D(
            vertices=vertices,
            faces=faces
        )

class TriangleMesh3D(TriangleMesh):
    def __init__(self, 
                 vertices, 
                 faces, 
                 id = -1, 
                 visited = False
                 ):
        super().__init__(
            vertices = vertices, 
            faces = faces, 
            id = id, 
            visited = visited, 
            dim = 3
        )
    
    @staticmethod
    def from_file_path(file_path: str) -> "TriangleMesh3D":
        vertices, faces = load_mesh(file_path, dim=3)
        return TriangleMesh3D(
            vertices=vertices,
            faces=faces
        )