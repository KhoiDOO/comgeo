from .base import Mesh
from .primitives.face import Face
from .primitives.quad_face import QuadFace
from .primitives.triangle_face import TriangleFace
from ..vertex import Vertex2D, Vertex3D
from ...functional.mesh.io.load import load_mesh

from ..utils.error import check_type


class HybridMesh(Mesh):
    def __init__(self, 
        vertices: list[Vertex2D | Vertex3D], 
        faces: list[list[int]],
        id: int = -1, 
        visited: bool = False,
        face_type: type[Face] | type[QuadFace] | type[TriangleFace] = Face,
        dim: int = 2 
    ):  
        super().__init__(vertices, faces, id, visited)

        if dim == 2:
            check_type(vertices[0], Vertex2D, "vertices")
        elif dim == 3:
            check_type(vertices[0], Vertex3D, "vertices")
        else:
            raise ValueError("dim must be 2 or 3")

        self._faces = [face_type(face) for face in faces]
    
    @staticmethod
    def from_file_path(file_path: str, dim: int = 2) -> 'HybridMesh':
        vertices, faces = load_mesh(file_path, dim)
        return HybridMesh(vertices, faces, dim=dim)