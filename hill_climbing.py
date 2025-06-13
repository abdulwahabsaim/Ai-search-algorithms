def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        neighbors = [n for n in graph.get(current, []) if n not in visited]
        if not neighbors:
            return path  # No better neighbors, local maximum

        next_node = min(neighbors, key=lambda n: heuristic[n])

        if heuristic[next_node] >= heuristic[current]:
            return path  # No improvement

        current = next_node
        visited.add(current)
        path.append(current)

    return path

# Example graph with heuristic values
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 1,
    'E': 2,
    'F': 0
}

print(hill_climbing(graph, 'A', 'F', heuristic))  # Output: path or partial path
