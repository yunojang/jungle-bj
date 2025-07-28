import sys
from collections import defaultdict
input = sys.stdin.readline 

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    p, a, b = tuple(input().split())
    for _ in range(2):
        graph[p].append(None)
    if a != '.':
        graph[p][0] = a
    if b != '.':
        graph[p][1] = b
    
def pre_order(c):
    print(c, end='')
    for child in graph[c]:
        if child is not None: 
            pre_order(child)

def in_order(c):
    if graph[c][0] is not None: in_order(graph[c][0])
    print(c, end='')
    if graph[c][1] is not None: in_order(graph[c][1])

def post_order(c):
    for child in graph[c]:
        if child is not None: 
            post_order(child)
    print(c, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
