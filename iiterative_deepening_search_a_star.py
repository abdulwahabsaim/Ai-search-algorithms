import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def depth_limited_astar(grid, current, goal, g, limit, path, visited):
    if current == goal:
        return path
    if g + heuristic(current, goal) > limit:
        return None

    visited.add(current)
    x, y = current
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        neighbor = (nx, ny)
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and neighbor not in visited:
            result = depth_limited_astar(grid, neighbor, goal, g + 1, limit, path + [neighbor], visited)
            if result:
                return result
    visited.remove(current)
    return None

def ids_astar(grid, start, goal):
    limit = heuristic(start, goal)
    while True:
        visited = set()
        result = depth_limited_astar(grid, start, goal, 0, limit, [start], visited)
        if result:
            return result
        limit += 1

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

print(ids_astar(grid, start, goal))  # Output: path from start to goal
