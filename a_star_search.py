import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = [(heuristics[start], 0, start, [start])]  # (f = g + h, g, node, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor, cost in graph.get(current, []):
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + heuristics[neighbor]
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    return None

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

print(a_star_search(graph, heuristics, 'A', 'F'))  # Output: ['A', 'B', 'E', 'F']
