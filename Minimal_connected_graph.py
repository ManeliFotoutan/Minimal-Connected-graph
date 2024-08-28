import networkx as nx
import matplotlib.pyplot as plt

# Function to draw and save the graph
def draw_graph(graph, mst_edges=None, title="Graph", filename="graph.png"):
    pos = nx.spring_layout(graph)  # positions for all nodes

    # Draw nodes and labels
    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color="lightblue")
    nx.draw_networkx_labels(graph, pos)

    # Draw edges with weights
    if mst_edges:
        # Draw MST edges in a different color
        mst_graph = nx.DiGraph()
        mst_graph.add_edges_from(mst_edges)
        nx.draw_networkx_edges(graph, pos, edgelist=mst_graph.edges(), edge_color='r', arrows=True, width=2)
        edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True) if (u, v) in mst_edges}
    else:
        nx.draw_networkx_edges(graph, pos, arrows=True)
        edge_labels = nx.get_edge_attributes(graph, 'weight')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.savefig(filename)
    plt.clf()  # Clear the current figure to prevent overlap when drawing the next graph

# Function to find minimum spanning arborescence using Edmonds' algorithm with constraints
def min_spanning_arborescence(graph, root, max_edges_per_node=None, excluded_edges=None):
    arborescence = nx.algorithms.tree.branchings.Edmonds(graph)

    if max_edges_per_node is None:
        max_edges_per_node = {}
    if excluded_edges is None:
        excluded_edges = set()

    # Remove excluded edges from the graph
    for u, v in excluded_edges:
        if graph.has_edge(u, v):
            graph.remove_edge(u, v)

    # Find the MSA with constraints
    mst = arborescence.find_optimum(attr='weight', default=0, kind='min', style='arborescence', preserve_attrs=True)

    # Filter edges based on max_edges_per_node constraint
    final_edges = []
    edge_count = {node: 0 for node in graph.nodes()}

    for u, v, d in mst.edges(data=True):
        if u in max_edges_per_node and edge_count[u] >= max_edges_per_node[u]:
            continue
        if v in max_edges_per_node and edge_count[v] >= max_edges_per_node[v]:
            continue
        
        final_edges.append((u, v, d))
        edge_count[u] += 1
        edge_count[v] += 1

    return final_edges

# Create a directed graph with weights
G = nx.DiGraph()
G.add_edge(0, 1, weight=10)
G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=3)
G.add_edge(3, 1, weight=2)
G.add_edge(1, 3, weight=1)

# Draw and save the input graph
draw_graph(G, title="Input Directed Weighted Graph", filename="input_graph.png")

# Define constraints
root = 0
max_edges_per_node = {1: 2, 2: 1}  # Example: node 1 can have at most 2 edges, node 2 can have at most 1 edge
excluded_edges = {(3, 1), (1, 3)}  # Example: exclude edges (3, 1) and (1, 3)

# Find the Minimum Spanning Arborescence with constraints
mst_edges = min_spanning_arborescence(G, root, max_edges_per_node=max_edges_per_node, excluded_edges=excluded_edges)

# Draw and save the Minimum Spanning Arborescence
draw_graph(G, mst_edges=mst_edges, title="Minimum Spanning Arborescence", filename="msa_graph.png")


#test for pushing