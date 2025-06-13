def hill_climbing(grid, start, goal):
    from heapq import heappush, heappop

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        x, y = current
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    heappush(neighbors, (heuristic(neighbor, goal), neighbor))

        if not neighbors:
            return path  # stuck at local maximum

        _, next_node = heappop(neighbors)
        if heuristic(next_node, goal) >= heuristic(current, goal):
            return path  # no better neighbor

        current = next_node
        visited.add(current)
        path.append(current)

    return path

# Example grid (0 = free, 1 = obstacle):
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

print(hill_climbing(grid, start, goal))  # Output: path from start or partial if stuck
