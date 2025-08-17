import os
import math
import matplotlib.pyplot as plt
from comgeo.core.polygon.base import Polygon
from comgeo.core.vertex import Vertex2D

def plot_polygon(polygon: Polygon, title: str, filename: str):
    """Plots a polygon and saves it to a file."""
    plt.figure()
    
    # Extract x and y coordinates
    x_coords = [v.x for v in polygon.vertices]
    y_coords = [v.y for v in polygon.vertices]
    
    # Add the first vertex to the end to close the polygon
    x_coords.append(polygon.vertices[0].x)
    y_coords.append(polygon.vertices[0].y)
    
    plt.plot(x_coords, y_coords, 'b-')
    plt.scatter([v.x for v in polygon.vertices], [v.y for v in polygon.vertices], c='red')
    
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis('equal')
    
    # Save the plot to a file
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, filename))
    plt.close()

if __name__ == "__main__":
    # 1. Create a convex polygon (a regular dodecagon)
    num_vertices = 12
    radius = 10
    convex_vertices = []
    for i in range(num_vertices):
        angle = 2 * math.pi * i / num_vertices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        convex_vertices.append(Vertex2D(x, y))
    convex_polygon = Polygon(convex_vertices)

    # 2. Create a non-convex polygon
    non_convex_vertices = convex_vertices[:]
    # Move one vertex towards the center to make it non-convex
    non_convex_vertices[6] = Vertex2D(0.0, 0.0)
    non_convex_polygon = Polygon(non_convex_vertices)

    # 3. Plot the polygons and save them
    convex_result = convex_polygon.is_convex()
    plot_polygon(convex_polygon, f"Convex Polygon (is_convex: {convex_result})", "convex_polygon.pdf")

    non_convex_result = non_convex_polygon.is_convex()
    plot_polygon(non_convex_polygon, f"Non-Convex Polygon (is_convex: {non_convex_result})", "non_convex_polygon.pdf")

    print("Plots saved to 'convex_polygon.pdf' and 'non_convex_polygon.pdf'")

