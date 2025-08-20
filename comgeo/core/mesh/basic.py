from .hybrid import HybridMesh
from .primitives.face import Face
from .primitives.quad_face import QuadFace
from .primitives.triangle_face import TriangleFace
from ..vertex import Vertex2D, Vertex3D

from ..utils.error import check_type
from ...functional.mesh.io.load import load_mesh

from ...constant import EIGHTY_WORKERS

import multiprocessing


class BasicMesh(HybridMesh):
    def __init__(self, 
        vertices: list[Vertex2D | Vertex3D], 
        faces: list[list[int]],
        id: int = -1, 
        visited: bool = False,
        face_type: type[QuadFace] | type[TriangleFace] = TriangleFace,
        dim: int = 2
    ):
        super().__init__(vertices, faces, id, visited, face_type, dim)

        check_type(face_type, (type(QuadFace), type(TriangleFace)), "face_type")

    @staticmethod
    def from_file_path(
        file_path: str, 
        dim: int, 
        face_type: type[QuadFace] | type[TriangleFace]
    ) -> "BasicMesh":
        vertices, faces = load_mesh(file_path, dim)
        return BasicMesh(
            vertices=vertices,
            faces=faces,
            face_type=face_type,
            dim=dim
        )

    @staticmethod
    def _face_area(args):
        face: Face = args[0]
        vertices: list[Vertex2D | Vertex3D] = args[1]
        return face.area(vertices)
    
    @staticmethod
    def _sample_points(args):
        face: Face = args[0]
        num: int = args[1]
        vertices: list[Vertex2D | Vertex3D] = args[2]
        return face.point_cloud_sampling(num, vertices)
        
    def point_cloud_sampling(self, num_points: int) -> list[Vertex2D | Vertex3D]:
        with multiprocessing.Pool(EIGHTY_WORKERS) as pool:
            face_areas = pool.map(
                BasicMesh._face_area,
                [(face, self._vertices) for face in self._faces]
            )

        total_area = sum(face_areas)
        probabilities = [area / total_area for area in face_areas]

        # Split num_points for each face based on area, ensure at least 1 point per face
        points_per_face = [max(1, int(round(p * num_points))) for p in probabilities]

        # Adjust total points to match num_points exactly
        diff = sum(points_per_face) - num_points
        if diff != 0:
            # Sort faces by fractional part of their probability for adjustment
            fractional = [(i, (probabilities[i] * num_points) % 1) for i in range(len(probabilities))]
            fractional.sort(key=lambda x: x[1], reverse=(diff > 0))
            for i in range(abs(diff)):
                idx = fractional[i][0]
                points_per_face[idx] -= 1 if diff > 0 else -1

        # Use multiprocessing to sample points from faces in parallel
        with multiprocessing.Pool(EIGHTY_WORKERS) as pool:
            sampled_points_lists = pool.map(
                self._sample_points,
                [(self._faces[i], points_per_face[i], self._vertices) for i in range(len(self._faces))]
            )

        sampled_points = []
        for pts in sampled_points_lists:
            sampled_points.extend(pts)

        return sampled_points