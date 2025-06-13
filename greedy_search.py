import heapq

def greedy_search(graph, heuristics, start, goal):
    visited = set()
    queue = [(heuristics[start], start, [start])]

    while queue:
        _, current, path = heapq.heappop(queue)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristics = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

print(greedy_search(graph, heuristics, 'A', 'F'))  # Output: ['A', 'C', 'F']
