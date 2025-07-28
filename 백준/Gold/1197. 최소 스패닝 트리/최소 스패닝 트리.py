import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
v, e = tuple(map(int, input().split()))

graph = defaultdict(list)
for _ in range(e):
    source, dest, cost = tuple(map(int, input().split()))
    graph[source].append((dest, cost))
    graph[dest].append((source, cost))

visited = set()
pq = [(0,1)]
total_cost = 0

while pq and len(visited) < v:
    cost, to  = heapq.heappop(pq)
    if to in visited:
        continue
    visited.add(to)
    total_cost += cost
    for next, c in graph[to]:
        heapq.heappush(pq, (c,next))


print(total_cost)