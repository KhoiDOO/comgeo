from ...core.vertex import Vertex, Vertex2D, Vertex3D

from random import random
import math

def point_cloud_sampling_triangle(vertices: list[Vertex | Vertex2D | Vertex3D], num_points: int) -> list[Vertex | Vertex2D | Vertex3D]:
    if type(vertices[0]) not in [Vertex2D, Vertex3D]:
        raise NotImplementedError("point_cloud_sampling not implemented for " + str(type(vertices[0])))
    
    points: list[Vertex2D | Vertex3D] = []
    for _ in range(num_points):
        r1 = random()
        r2 = random()

        w1 = 1 - math.sqrt(r1)
        w2 = math.sqrt(r1) * (1 - r2)
        w3 = math.sqrt(r1) * r2

        points.append(
            vertices[0] * w1 + \
            vertices[1] * w2 + \
            vertices[2] * w3
        )
    
    return points

def point_cloud_sampling_quad(vertices: list[Vertex | Vertex2D | Vertex3D], num_points: int) -> list[Vertex | Vertex2D | Vertex3D]:
    if type(vertices[0]) not in [Vertex2D, Vertex3D]:
        raise NotImplementedError("point_cloud_sampling not implemented for " + str(type(vertices[0])))
    
    points: list[Vertex2D | Vertex3D] = []
    for _ in range(num_points):
        l = random()
        r = random()

        a1 = (1 - l) * (1 - r)
        a2 = l * (1 - r)
        a3 = l * r
        a4 = (1 - l) * r

        points.append(
            vertices[0] * a1 + \
            vertices[1] * a2 + \
            vertices[2] * a3 + \
            vertices[3] * a4
        )
    
    return points