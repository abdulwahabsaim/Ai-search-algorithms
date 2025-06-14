# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 02:29:50 2025

@author: shabi
"""

import heapq
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0
}


def best_first_search_tree(start, goal, tree, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    
    while pq:
        h, current = heapq.heappop(pq)
        print("Visited:", current)
        
        if current == goal:
            print("Goal reached!")
            return
        
        for neighbor in tree.get(current, []):
            heapq.heappush(pq, (heuristic[neighbor], neighbor))


best_first_search_tree('A', 'F', tree, heuristic)