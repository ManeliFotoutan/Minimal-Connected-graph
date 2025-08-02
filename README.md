# Minimal Connected Graph with Constraints

This project implements an algorithm to find a Minimum Spanning Arborescence (a directed spanning tree rooted at a specific node) in a weighted directed graph, with optional constraints on the number of edges per node and excluded edges.

## Description

- The program creates a directed graph with weighted edges.  
- It finds a minimum spanning arborescence using a union-find (disjoint set) data structure to avoid cycles.  
- Optional constraints allow limiting the maximum number of edges outgoing from or incoming to certain nodes.  
- Certain edges can be excluded from consideration.  
- The input graph and resulting minimum spanning arborescence are visualized and saved as PNG images.
## Usage

1. Run the script:

   \`\`\`bash
   python Solu/Minimal_connected_graph.py
   \`\`\`

The script generates two image files:

- input_graph.png: Shows the original graph.  
- msa_graph.png: Shows the minimum spanning arborescence with constraints.

Modify the script to set:

- root: The root node for the arborescence.  
- max_edges_per_node: A dictionary to set maximum allowed edges per node.  
- excluded_edges: A set or dictionary of edges to exclude.

## Dependencies

- networkx  
- matplotlib

Install dependencies using:

\`\`\`bash
pip install networkx matplotlib
\`\`\`

## Notes

- The visualization uses matplotlib and saves images to files.  
- The algorithm uses a union-find structure for cycle detection.  
- The script currently does not display plots interactively; images are saved to disk instead.
EOF
