import networkx as nx

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

edges_with_weights = [
    ("Station A", "Station B", 5),
    ("Station B", "Station C", 3),
    ("Station C", "Station D", 4),
    ("Station D", "Station E", 2),
    ("Station E", "Station F", 6),
    ("Station B", "Station D", 7),
    ("Station A", "Station D", 9),
    ("Station C", "Station F", 8)
]
G.add_weighted_edges_from(edges_with_weights)

print("Ребра графа з вагами:")
for u, v, weight in G.edges(data=True):
    print(f"({u}, {v}) -> вага: {weight['weight']}")

# Використовуємо алгоритм Дейкстри для пошуку найкоротших шляхів
# від "Station A" до всіх інших вершин
shortest_paths = nx.single_source_dijkstra_path(G, source="Station A")
shortest_distances = nx.single_source_dijkstra_path_length(
    G, source="Station A"
    )

print("\nНайкоротші шляхи від Station A:")
for target in stations:
    print(
        (f"До {target}: шлях {shortest_paths[target]}, "
         f"відстань {shortest_distances[target]}")
    )
