import matplotlib.pyplot as plt
import networkx as nx

n = 50
k = 3

G = nx.random_regular_graph(k, n)

plt.figure(figsize=(8, 8))
nx.draw(
    G,
    with_labels=True,
    node_color="orange",
    node_size=300,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
)

plt.show()
