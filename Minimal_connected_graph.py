import networkx as nx
import matplotlib.pyplot as plt

# Function to draw the graph
def draw_graph(G, mst_edges=None, title="", filename="graph.png"):
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if mst_edges:
        mst = nx.DiGraph()
        mst.add_edges_from(mst_edges)
        nx.draw_networkx_edges(mst, pos, edgelist=mst_edges, edge_color='r', width=2)
    
    plt.title(title)
    plt.savefig(filename)
    plt.show()

# Function to find the Minimum Spanning Arborescence
def min_spanning_arborescence(G, root, max_edges_per_node=None, excluded_edges=None):
    if max_edges_per_node is None:
        max_edges_per_node = {}
    if excluded_edges is None:
        excluded_edges = set()
    
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    parent = {node: node for node in G.nodes()}
    rank = {node: 0 for node in G.nodes()}
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    mst_edges = []
    for u, v, data in edges:
        if (u, v) in excluded_edges or (v, u) in excluded_edges:
            continue
        if find(u) != find(v):
            if u in max_edges_per_node and len([e for e in mst_edges if e[0] == u]) >= max_edges_per_node[u]:
                continue
            if v in max_edges_per_node and len([e for e in mst_edges if e[1] == v]) >= max_edges_per_node[v]:
                continue
            union(u, v)
            mst_edges.append((u, v, data))
    
    return mst_edges

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
max_edges_per_node = {}  # Example: node 1 can have at most 2 edges, node 2 can have at most 1 edge
excluded_edges = {}  # Example: exclude edges (3, 1) and (1, 3)

# Find the Minimum Spanning Arborescence with constraints
mst_edges = min_spanning_arborescence(G, root, max_edges_per_node=max_edges_per_node, excluded_edges=excluded_edges)

# Draw and save the Minimum Spanning Arborescence
draw_graph(G, mst_edges=mst_edges, title="Minimum Spanning Arborescence", filename="msa_graph.png")
