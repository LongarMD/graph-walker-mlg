import networkx as nx
import numpy as np

import mlg_walker as walker

G = nx.karate_club_graph()
walks = walker.random_walks(
    G, n_walks=100, walk_len=50,
    sub_sampling=0.5)
