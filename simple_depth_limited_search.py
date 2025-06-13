def dls(graph, start, limit, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    if limit <= 0:
        return order
    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dls(graph, neighbor, limit-1, visited))
    return order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dls(graph, 'A', 2))  # Output: ['A', 'B', 'D', 'E', 'C', 'F']
