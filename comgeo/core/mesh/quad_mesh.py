from .basic import BasicMesh
from .primitives.quad_face import QuadFace

from ...functional.mesh.io.load import load_mesh

class QuadMesh(BasicMesh):
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
            face_type = QuadFace, 
            dim = dim
        )

    @staticmethod
    def from_file_path(file_path: str, dim: int = 2) -> "QuadMesh":
        vertices, faces = load_mesh(file_path, dim)
        return QuadMesh(
            vertices=vertices,
            faces=faces,
            dim=dim
        )

class QuadMesh2D(QuadMesh):
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
    def from_file_path(file_path: str) -> "QuadMesh2D":
        vertices, faces = load_mesh(file_path, dim=2)
        return QuadMesh2D(
            vertices=vertices,
            faces=faces
        )

class QuadMesh3D(QuadMesh):
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
    def from_file_path(file_path: str) -> "QuadMesh3D":
        vertices, faces = load_mesh(file_path, dim=3)
        return QuadMesh3D(
            vertices=vertices,
            faces=faces
        )
