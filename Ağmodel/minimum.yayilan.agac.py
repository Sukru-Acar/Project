
import networkx as nx

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('A', 'D', 5),
    ('B', 'D', 10),
    ('C', 'D', 3),
    ('C', 'E', 8),
    ('D', 'E', 4),
    ('D', 'F', 6),
    ('E', 'F', 1)
]
G = nx.Graph()
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

print("Minimum Yayılan Ağaç:")
for edge in mst.edges(data=True):
    print(edge)
