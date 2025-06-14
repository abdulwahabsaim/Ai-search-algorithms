import heapq
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],  
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 0
}

def best_first_search_graph(start, goal, graph, heuristic):
    pq = []
    visited = set()
    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        h, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        print("Visited:", current)

        if current == goal:
            print("Goal reached!")
            return

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

best_first_search_graph('A', 'F', graph, heuristic)
