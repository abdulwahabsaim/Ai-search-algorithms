import heapq

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start)]  # (cost, node)

    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))
    return float('inf')  # Goal not reachable

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

print(ucs(graph, 'A', 'F'))  # Output: 7
