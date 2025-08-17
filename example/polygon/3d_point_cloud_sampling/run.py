import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from comgeo.core.polygon.triangle import Triangle
from comgeo.core.polygon.quad import Quad
from comgeo.core.vertex import Vertex3D

def plot_3d_point_cloud(polygon, points, title: str, filename: str):
    """Plots the 3D polygon, its vertices, and the sampled points."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot polygon surface
    poly_verts = [[(v.x, v.y, v.z) for v in polygon.vertices]]
    ax.add_collection3d(Poly3DCollection(poly_verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Plot polygon vertices
    vert_x = [v.x for v in polygon.vertices]
    vert_y = [v.y for v in polygon.vertices]
    vert_z = [v.z for v in polygon.vertices]
    ax.scatter(vert_x, vert_y, vert_z, c='red', s=50, label='Vertices')

    # Plot sampled points
    point_x = [p.x for p in points]
    point_y = [p.y for p in points]
    point_z = [p.z for p in points]
    ax.scatter(point_x, point_y, point_z, c='green', s=10, label='Sampled Points')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.legend()

    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, filename))
    plt.close()

if __name__ == "__main__":
    # 3D Triangle
    triangle_vertices = [
        Vertex3D(1.0, 0.0, 0.0),
        Vertex3D(0.0, 1.0, 0.0),
        Vertex3D(0.0, 0.0, 1.0)
    ]
    triangle = Triangle(triangle_vertices)
    triangle_points = triangle.point_cloud_sampling(100)
    plot_3d_point_cloud(triangle, triangle_points, "3D Triangle Point Cloud Sampling", "3d_triangle_point_cloud.pdf")

    # 3D Quad
    quad_vertices = [
        Vertex3D(0.0, 0.0, 0.0),
        Vertex3D(1.0, 0.0, 1.0),
        Vertex3D(1.0, 1.0, 1.0),
        Vertex3D(0.0, 1.0, 0.0)
    ]
    quad = Quad(quad_vertices)
    quad_points = quad.point_cloud_sampling(100)
    plot_3d_point_cloud(quad, quad_points, "3D Quad Point Cloud Sampling", "3d_quad_point_cloud.pdf")

    print("Plots saved to '3d_triangle_point_cloud.pdf' and '3d_quad_point_cloud.pdf'")