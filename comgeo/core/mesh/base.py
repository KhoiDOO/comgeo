from ..graph import Graph
from ..vertex import Vertex2D, Vertex3D
from ...decorator.error import not_instance, not_self_implemented
from ..utils.error import check_type, check_consistency

import numpy as np


class Mesh(Graph):
    def __init__(self, 
        vertices: list[Vertex2D | Vertex3D], 
        faces: list[list[int]],
        id: int = -1, 
        visited: bool = False
    ):  
        super().__init__(vertices, id, visited)
        
        if type(self._vertices[0]) not in [Vertex2D, Vertex3D]:
            raise ValueError("Vertices must be of type Vertex2D or Vertex3D")

        check_type(faces, list, "faces")
        check_consistency(faces, "faces")
        self.check_faces_len(faces)
        self._faces = faces

        self._face_adjacency_matrix: np.ndarray = np.zeros((len(faces), len(faces)))
        self._connected_components: list[list[int]] = []
        self._vertex2face: list[list[int]] = []
        self._vertex2cc: list[int] = []
    
    @not_self_implemented
    @staticmethod
    def from_file_path(file_path: str) -> 'Mesh':
        pass

    @staticmethod
    def check_faces_len(faces: list[list[int]]):
        if len(faces) == 0:
            raise ValueError("Mesh must have at least one face")
    
    @property
    def faces(self):
        return self._faces
    
    @faces.setter
    @not_instance(list)
    def faces(self, faces: list[list[int]]):
        check_type(faces, list, "faces")
        check_consistency(faces, "faces")
        self.check_faces_len(faces)
        self._faces = faces
    
    @property
    def face_adjacency_matrix(self) -> np.ndarray:
        return self._face_adjacency_matrix
    
    @property
    def has_face_adjacency_matrix(self) -> bool:
        return np.sum(self._face_adjacency_matrix) > 0
    
    @not_self_implemented
    def construct_face_adjacency_matrix(self) -> np.ndarray:
        pass
    
    @property
    def connected_components(self) -> list[list[int]]:
        return self._connected_components
    
    @property
    def has_connected_components(self) -> bool:
        return len(self._connected_components) > 0
    
    @not_self_implemented
    def construct_connected_components(self) -> list[list[int]]:
        pass
    
    @property
    def vertex2face(self) -> list[list[int]]:
        return self._vertex2face
    
    @property
    def has_vertex2face(self) -> bool:
        return len(self._vertex2face) > 0
    
    @not_self_implemented
    def construct_vertex2face(self) -> list[list[int]]:
        pass
    
    @property
    def vertex2cc(self) -> list[int]:
        return self._vertex2cc
    
    @property
    def has_vertex2cc(self) -> bool:
        return len(self._vertex2cc) > 0
    
    @not_self_implemented
    def construct_vertex2cc(self) -> list[int]:
        pass
    
    @property
    def vertex_adjacency_matrix(self) -> np.ndarray:
        return self._adjacency_matrix
    
    @property
    def has_vertex_adjacency_matrix(self) -> bool:
        return np.sum(self._adjacency_matrix) > 0
    
    @not_self_implemented
    def construct_vertex_adjacency_matrix(self) -> np.ndarray:
        pass
    
    @property
    def vertex_adjacency_list(self) -> list[list[int]]:
        return self._adjacency_list
    
    @property
    def has_vertex_adjacency_list(self) -> bool:
        return len(self._adjacency_list) > 0
    
    @not_self_implemented
    def construct_vertex_adjacency_list(self) -> list[list[int]]:
        pass

    @not_self_implemented
    def point_cloud_sampling(self, num_points: int) -> list[Vertex2D | Vertex3D]:
        pass

    @not_self_implemented
    def visualize(self):
        pass