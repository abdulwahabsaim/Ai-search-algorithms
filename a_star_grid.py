import heapq

def a_star(grid, start, goal):
    # Manhattan distance
    h = lambda p: abs(p[0]-goal[0]) + abs(p[1]-goal[1])
    # open set: (f, g, position, path)
    openq = [(h(start), 0, start, [start])]
    seen = set()

    while openq:
        f, g, node, path = heapq.heappop(openq)
        if node == goal:
            return path
        if node in seen:
            continue
        seen.add(node)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nxt = (node[0]+dx, node[1]+dy)
            if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]) and grid[nxt[0]][nxt[1]] == 0:
                heapq.heappush(openq, (g+1 + h(nxt), g+1, nxt, path + [nxt]))

    return None

# Example
grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]
print(a_star(grid, (0,0), (4,4)))  # e.g., path list

