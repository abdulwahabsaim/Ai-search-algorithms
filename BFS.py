# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 01:25:31 2025

@author: shabi
"""

tree = {
        '5' : ['3','7'],
        '3' : ['2','4'],
        '7' : ['8'],
        '2' : [],
        '4' : [],
        '8' : []
        }
visit = []
remaining = []
def bfs(visit,tree,node):
    visit.append(node)
    remaining.append(node)
    while remaining:
        x = remaining.pop(0)
       # print(x)
        for child in tree[x]:
            if child not in visit:
                visit.append(child)
                remaining.append(child)
            print(remaining)
    print("Visit List : ",visit)
    print("Remaining List : ",remaining)
    
bfs(visit, tree, '5')
            