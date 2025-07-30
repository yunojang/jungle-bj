import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = list(map(int, input().split()))

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = tuple(map(int, input().split()))
    graph[u].append(v)

visited = [0] * (n + 1)
q = deque([x])

while q:
    cur = q.popleft()
    dist = visited[cur]
    for adj in graph[cur]:
        if visited[adj] > 0:
            continue
        q.append(adj)
        visited[adj] = dist + 1

has_k = False
visited[x] = 0
for i in range(1, n + 1):
    dist = visited[i]
    if dist == k:
        has_k = True
        print(i)

if not has_k:
    print(-1)
