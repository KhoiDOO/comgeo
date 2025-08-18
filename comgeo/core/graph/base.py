from ..vertex import Vertex, Vertex2D, Vertex3D
from ...decorator.error import not_instance, not_self_implemented
from ..utils.error import check_type, check_consistency

import numpy as np


class Graph:
    def __init__(self, 
        vertices: list[Vertex | Vertex2D | Vertex3D], 
        id: int = -1, 
        visited: bool = False
    ):
        check_type(vertices, list, "vertices")
        self.check_vertices_len(vertices)
        check_consistency(vertices, "vertices")
        check_type(id, int, "id")
        check_type(visited, bool, "visited")
        
        self._vertices = vertices
        self._id = id
        self._visited = visited

        self._adjacency_list: dict[int, list[int]] = {}
        self._adjacency_matrix: np.ndarray = np.zeros((len(vertices), len(vertices)))
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    @not_instance(int)
    def id(self, id: int):
        self._id = id
    
    @property
    def visited(self):
        return self._visited
    
    @visited.setter
    @not_instance(bool)
    def visited(self, visited: bool):
        self._visited = visited
    
    @property
    def has_adjacency_list(self):
        return len(self._adjacency_list) > 0
    
    @property
    def has_adjacency_matrix(self):
        return np.sum(self._adjacency_matrix) > 0
    
    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    @not_instance(list)
    def vertices(self, vertices: list[Vertex | Vertex2D | Vertex3D]):
        self.check_vertices_len(vertices)
        self._vertices = vertices
    
    @staticmethod
    def check_vertices_len(vertices: list[Vertex | Vertex2D | Vertex3D]):
        if len(vertices) == 0:
            raise ValueError("Graph must have at least one vertex")
    
    @property
    def adjacency_list(self):
        return self._adjacency_list
    
    @property
    def adjacency_matrix(self):
        return self._adjacency_matrix
    
    @adjacency_matrix.setter
    @not_instance(np.ndarray)
    def adjacency_matrix(self, adjacency_matrix: np.ndarray):
        self._adjacency_matrix = adjacency_matrix
    
    @adjacency_list.setter
    @not_instance(dict)
    def adjacency_list(self, adjacency_list: dict[int, list[int]]):
        self._adjacency_list = adjacency_list
    
    def add_vertex(self, vertex: Vertex | Vertex2D | Vertex3D, connections: list[int] = []):
        check_type(vertex, type(self._vertices[0]), "vertex")
        check_type(connections, list, "connections")
        check_consistency(connections, "connections")

        self._vertices.append(vertex)
        self._adjacency_list[vertex.id] = connections
        self._adjacency_matrix = np.pad(self._adjacency_matrix, ((0, 1), (0, 1)), 'constant')
        for connection in connections:
            self._adjacency_matrix[-1, connection] = 1
            self._adjacency_matrix[connection, -1] = 1