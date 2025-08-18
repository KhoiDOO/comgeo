import matplotlib.pyplot as plt
import matplotlib.patches as patches
from comgeo.core.vertex import Vertex2D
from comgeo.functional.polygon.area import get_area
from comgeo.functional.polygon.center import get_center

def plot_polygon(vertices, ax, color='blue', label='Polygon'):
    """Plot a polygon given its vertices."""
    # Extract x and y coordinates
    x = [v.x for v in vertices]
    y = [v.y for v in vertices]
    
    # Close the polygon
    x.append(vertices[0].x)
    y.append(vertices[0].y)
    
    # Plot the polygon
    ax.plot(x, y, 'o-', color=color, label=label)
    ax.fill(x, y, alpha=0.2, color=color)
    
    # Add vertex labels
    for i, vertex in enumerate(vertices):
        ax.text(vertex.x, vertex.y, f'V{i+1}', fontsize=9, ha='right')

def main():
    # Create a triangle
    triangle = [
        Vertex2D(0.0, 0.0),
        Vertex2D(4.0, 0.0),
        Vertex2D(2.0, 4.0)
    ]
    
    # Create a quadrilateral
    quadrilateral = [
        Vertex2D(1.0, 1.0),
        Vertex2D(5.0, 1.0),
        Vertex2D(6.0, 4.0),
        Vertex2D(2.0, 5.0)
    ]
    
    # Calculate centers and areas
    triangle_center = get_center(triangle)
    triangle_area = get_area(triangle)
    
    quadrilateral_center = get_center(quadrilateral)
    quadrilateral_area = get_area(quadrilateral)
    
    print(f"Triangle - Center: ({triangle_center.x:.2f}, {triangle_center.y:.2f}), Area: {triangle_area:.2f}")
    print(f"Quadrilateral - Center: ({quadrilateral_center.x:.2f}, {quadrilateral_center.y:.2f}), "
          f"Area: {quadrilateral_area:.2f}")
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot triangle
    plot_polygon(triangle, ax1, 'blue', 'Triangle')
    ax1.plot(triangle_center.x, triangle_center.y, 'ro', label='Center')
    ax1.text(triangle_center.x, triangle_center.y, 
             f'({triangle_center.x:.2f}, {triangle_center.y:.2f})', 
             fontsize=9, ha='left', va='bottom')
    ax1.set_title(f'Triangle (Area: {triangle_area:.2f})')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.axis('equal')
    ax1.legend()
    ax1.grid(True)
    
    # Plot quadrilateral
    plot_polygon(quadrilateral, ax2, 'green', 'Quadrilateral')
    ax2.plot(quadrilateral_center.x, quadrilateral_center.y, 'ro', label='Center')
    ax2.text(quadrilateral_center.x, quadrilateral_center.y, 
             f'({quadrilateral_center.x:.2f}, {quadrilateral_center.y:.2f})', 
             fontsize=9, ha='left', va='bottom')
    ax2.set_title(f'Quadrilateral (Area: {quadrilateral_area:.2f})')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.axis('equal')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    
    # Save the figure
    output_path = '/home/khoi/git/computational-geometry/example/polygon/2d_center_area/polygons.pdf'
    plt.savefig(output_path, format='pdf', bbox_inches='tight')
    print(f"Plot saved to {output_path}")
    
    plt.show()

if __name__ == "__main__":
    main()