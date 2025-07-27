import sys 
input = sys.stdin.readline


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = tuple(map(int, input().split()))
    graph[s].append((e,c))
start, des = tuple(map(int, input().split()))
min_cost = [float('inf')] * (n+1)
min_cost[start] = 0

import heapq
pq = [(0, start)]
result = None

while pq:
    cost, cur = heapq.heappop(pq)
    if cur == des:
        result = cost
        break
    if min_cost[cur] < cost:
        continue
    for e, c in graph[cur]:
        new_cost = cost + c
        if new_cost < min_cost[e]:
            min_cost[e]= new_cost
            heapq.heappush(pq, (new_cost, e))

print(result)
