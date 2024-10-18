import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Station A",
    "Station B",
    "Station C",
    "Station D",
    "Station E",
    "Station F"
    ]
G.add_nodes_from(stations)

edges = [("Station A", "Station B"), ("Station B", "Station C"),
         ("Station C", "Station D"), ("Station D", "Station E"),
         ("Station E", "Station F"), ("Station B", "Station D"),
         ("Station A", "Station D"), ("Station C", "Station F")]
G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    font_weight='bold',
    node_size=2000
    )
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик графу
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:", dict(G.degree()))
