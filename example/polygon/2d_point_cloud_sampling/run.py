import os
import random
import matplotlib.pyplot as plt
from comgeo.core.polygon.triangle import Triangle
from comgeo.core.polygon.quad import Quad
from comgeo.core.vertex import Vertex2D

def create_random_vertices(num_vertices: int, max_coord: int = 100):
    """Creates a list of random 2D vertices."""
    return [Vertex2D(random.uniform(0, max_coord), random.uniform(0, max_coord)) for _ in range(num_vertices)]

def plot_point_cloud(polygon, points, title: str, filename: str):
    """Plots the polygon, its vertices, and the sampled points."""
    plt.figure()

    # Plot polygon edges
    poly_x = [v.x for v in polygon.vertices] + [polygon.vertices[0].x]
    poly_y = [v.y for v in polygon.vertices] + [polygon.vertices[0].y]
    plt.plot(poly_x, poly_y, 'b-', label='Polygon Edges')

    # Plot polygon vertices
    vert_x = [v.x for v in polygon.vertices]
    vert_y = [v.y for v in polygon.vertices]
    plt.scatter(vert_x, vert_y, c='red', s=50, label='Vertices', zorder=5)

    # Plot sampled points
    point_x = [p.x for p in points]
    point_y = [p.y for p in points]
    plt.scatter(point_x, point_y, c='green', s=10, label='Sampled Points')

    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, filename))
    plt.close()

if __name__ == "__main__":
    # Triangle
    triangle_vertices = [
        Vertex2D(-1.0, 1.0),
        Vertex2D(5.0, 1.0),
        Vertex2D(0.0, -1.0),
    ]
    triangle = Triangle(triangle_vertices)
    triangle_points = triangle.point_cloud_sampling(100)
    plot_point_cloud(triangle, triangle_points, "Triangle Point Cloud Sampling", "triangle_point_cloud.pdf")

    # Quad
    quad_vertices = [
        Vertex2D(-3.0, -3.0),
        Vertex2D(-2.0, 2.0),
        Vertex2D(2.0, 4.0),
        Vertex2D(3.0, -2.0),
    ]
    quad = Quad(quad_vertices)
    quad_points = quad.point_cloud_sampling(100)
    plot_point_cloud(quad, quad_points, "Quad Point Cloud Sampling", "quad_point_cloud.pdf")

    print("Plots saved to 'triangle_point_cloud.pdf' and 'quad_point_cloud.pdf'")