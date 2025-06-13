def dls(graph, node, goal, limit, visited):
    if limit < 0:
        return False
    visited.append(node)
    if node == goal:
        return True
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, limit - 1, visited):
                return True
    visited.pop()
    return False

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        if dls(graph, start, goal, depth, visited):
            return visited
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

print(ids(graph, 'A', 'F', 3))  # Output: ['A', 'C', 'F']
