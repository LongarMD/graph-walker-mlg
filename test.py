import networkx as nx
import numpy as np

import mlg_walker as walker

# G = nx.karate_club_graph()
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'C', weight=0.5)
G.add_edge('A', 'C', weight=0.25)
G.add_edge('B', 'D', weight=0.1)
G.add_edge('B', 'E', weight=0.1)

G.add_node('A', date=5.0)
G.add_node('B', date=2.0)
G.add_node('C', date=3.0)
G.add_node('D', date=4.0)
G.add_node('E', date=5.0)


walks = walker.random_walks(
    G, n_walks=1, walk_len=100,
    sub_sampling=1, verbose=True, no_future=True)

print(walks)