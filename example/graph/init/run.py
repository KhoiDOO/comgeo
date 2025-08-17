import random
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

from comgeo.core.vertex import Vertex2D
from comgeo.core.graph import Graph

# --- Constants ---
SEED = 42
TITLE_FONT_SIZE = 28
LABEL_FONT_SIZE = 24
ANNOTATION_FONT_SIZE = 20
HEATMAP_ANNOT_SIZE = 24
MARKER_SIZE = 30

def plot_graph(ax, graph, title):
    """Helper function to plot a graph on a given axes."""
    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=20)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.tick_params(axis='both', which='both', length=0)  # Remove tick marks

    # Plot edges
    num_vertices = len(graph.vertices)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph.adjacency_matrix[i, j] == 1:
                v1 = graph.vertices[i]
                v2 = graph.vertices[j]
                ax.plot([v1.x, v2.x], [v1.y, v2.y], 'k-', lw=0.5)

    # Plot vertices
    x_coords = [v.x for v in graph.vertices]
    y_coords = [v.y for v in graph.vertices]
    ax.plot(x_coords, y_coords, 'o', color='skyblue', 
        markersize=MARKER_SIZE, zorder=3, markeredgecolor='white', markeredgewidth=0.5)

    # Add labels to vertices
    for vertex in graph.vertices:
        ax.text(vertex.x, vertex.y, str(vertex.id), ha='center', va='center', 
            fontsize=ANNOTATION_FONT_SIZE, color='white', fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.5)

def run():
    """Generate and plot a random graph, then add two vertices."""
    # Set seed for reproducibility
    random.seed(SEED)
    np.random.seed(SEED)
    num_vertices = 10
    edge_probability = 0.1

    # 1. Create vertices with random coordinates
    vertices = [
        Vertex2D(x=random.uniform(0, 100), y=random.uniform(0, 100), id=i)
        for i in range(num_vertices)
    ]

    # 2. Initialize the graph
    graph = Graph(vertices=vertices)

    # 3. Create a random adjacency matrix
    adj_matrix = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < edge_probability:
                adj_matrix[i, j] = 1
                adj_matrix[j, i] = 1  # For an undirected graph
    graph.adjacency_matrix = adj_matrix

    adj_matrix_before = graph.adjacency_matrix.copy()

    # 4. Add two new vertices and connect them to odd vertices
    new_vertices = [
        Vertex2D(x=random.uniform(0, 100), y=random.uniform(0, 100), id=num_vertices),
        Vertex2D(x=random.uniform(0, 100), y=random.uniform(0, 100), id=num_vertices + 1)
    ]
    graph_after_vertices = vertices + new_vertices
    num_vertices_after = len(graph_after_vertices)

    adj_matrix_after = np.zeros((num_vertices_after, num_vertices_after))
    adj_matrix_after[:num_vertices, :num_vertices] = adj_matrix_before

    for i in range(num_vertices):
        if i % 2 != 0:  # Connect to odd-ID vertices
            adj_matrix_after[i, num_vertices] = 1
            adj_matrix_after[num_vertices, i] = 1
        if i % 2 == 0:  # Connect to even-ID vertices
            adj_matrix_after[i, num_vertices + 1] = 1
            adj_matrix_after[num_vertices + 1, i] = 1

    graph_after = Graph(vertices=graph_after_vertices)
    graph_after.adjacency_matrix = adj_matrix_after

    graph_after.add_vertex(
        Vertex2D(x=random.uniform(0, 100), y=random.uniform(0, 100), id=num_vertices_after),
        connections=[0, 2, 4]
    )
    adj_matrix_after = graph_after.adjacency_matrix

    # 5. Save the plots to a PDF
    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, 'graph_output.pdf')
    with PdfPages(output_path) as pdf:
        # Page 1: Graph before and after
        fig_graphs, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        plot_graph(ax1, graph, 'Graph Before')
        plot_graph(ax2, graph_after, 'Graph After')
        pdf.savefig(fig_graphs)
        plt.close(fig_graphs)

        # Page 2: Adjacency matrix before and after as heatmaps
        fig_matrices, (ax_m1, ax_m2) = plt.subplots(1, 2, figsize=(22, 10))

        vertex_ids_before = [v.id for v in graph.vertices]
        sns.heatmap(adj_matrix_before.astype(int), ax=ax_m1, annot=True, fmt='d', cmap='Blues', cbar=False,
                    xticklabels=vertex_ids_before, yticklabels=vertex_ids_before, annot_kws={"size": HEATMAP_ANNOT_SIZE})
        ax_m1.set_title('Adjacency Matrix Before', fontsize=TITLE_FONT_SIZE, pad=20)
        ax_m1.set_xlabel('Vertex ID', fontsize=LABEL_FONT_SIZE, labelpad=10)
        ax_m1.set_ylabel('Vertex ID', fontsize=LABEL_FONT_SIZE, labelpad=10)
        ax_m1.tick_params(axis='both', which='major', labelsize=LABEL_FONT_SIZE)

        vertex_ids_after = [v.id for v in graph_after.vertices]
        sns.heatmap(adj_matrix_after.astype(int), ax=ax_m2, annot=True, fmt='d', cmap='Blues', cbar=False,
                    xticklabels=vertex_ids_after, yticklabels=vertex_ids_after, annot_kws={"size": HEATMAP_ANNOT_SIZE})
        ax_m2.set_title('Adjacency Matrix After', fontsize=TITLE_FONT_SIZE, pad=20)
        ax_m2.set_xlabel('Vertex ID', fontsize=LABEL_FONT_SIZE, labelpad=10)
        ax_m2.set_ylabel('Vertex ID', fontsize=LABEL_FONT_SIZE, labelpad=10)
        ax_m2.tick_params(axis='both', which='major', labelsize=LABEL_FONT_SIZE)

        plt.tight_layout()
        pdf.savefig(fig_matrices)
        plt.close(fig_matrices)

    print(f"Graph and adjacency matrix have been exported to {output_path}")

if __name__ == "__main__":
    run()
