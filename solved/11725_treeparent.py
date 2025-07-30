import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    s, e = tuple(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

q = deque([1])
visited = [False] * (n + 1)
parents = [None] * (n + 1)
while q:
    cur = q.popleft()
    visited[cur] = True
    for adj in graph[cur]:
        if not visited[adj]:
            q.append(adj)
            parents[adj] = cur

for parent in parents:
    if parent:
        print(parent)
