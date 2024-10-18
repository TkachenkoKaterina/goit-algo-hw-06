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

edges = [("Station A", "Station B"), ("Station B", "Station C"),
         ("Station C", "Station D"), ("Station D", "Station E"),
         ("Station E", "Station F"), ("Station B", "Station D"),
         ("Station A", "Station D"), ("Station C", "Station F")]
G.add_edges_from(edges)


# шлях від Station A до Station F за допомогою DFS
def dfs_path(graph, start, target):
    predecessors = nx.dfs_predecessors(graph, start)
    path = [target]
    while target in predecessors:
        target = predecessors[target]
        path.append(target)
    return path[::-1]


dfs_path_result = dfs_path(G, "Station A", "Station F")
print("Шлях за допомогою DFS:", dfs_path_result)

# шлях від Station A до Station F за допомогою BFS
bfs_path = list(
    nx.shortest_path(G, source="Station A", target="Station F")
    )
print("Шлях за допомогою BFS:", bfs_path)
