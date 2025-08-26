
import numpy as np
import matplotlib.pyplot as plt
from comgeo.core.vertex import Vertex2D
from comgeo.functional.shape.form import circumcircle_vertices
import os

def main():
    # Create three random 2D vertices
    np.random.seed(42)
    points = [Vertex2D(*np.random.uniform(-10, 10, 2)) for _ in range(3)]

    # Construct the circumcircle
    circle = circumcircle_vertices(tuple(points))

    # Prepare plot
    fig, ax = plt.subplots()

    # Draw the circumcircle
    circ = plt.Circle((circle.center.x, circle.center.y), circle.radius, fill=False, color='blue', linewidth=2)
    ax.add_patch(circ)

    # Draw the three vertices
    x = [p.x for p in points]
    y = [p.y for p in points]
    ax.scatter(x, y, color='red', zorder=5)

    # Annotate points
    for i, p in enumerate(points):
        ax.annotate(f'P{i+1}', (p.x, p.y), textcoords="offset points", xytext=(5,5), ha='center')

    # Set limits and aspect
    ax.set_aspect('equal')
    ax.set_xlim(min(x + [circle.center.x - circle.radius]) - 1, max(x + [circle.center.x + circle.radius]) + 1)
    ax.set_ylim(min(y + [circle.center.y - circle.radius]) - 1, max(y + [circle.center.y + circle.radius]) + 1)

    # Save to PDF in the same folder as this script
    pdf_path = os.path.join(os.path.dirname(__file__), "circumcircle.pdf")
    plt.savefig(pdf_path)
    plt.close()

    print(f"Saved plot to {pdf_path}")

if __name__ == "__main__":
    main()
