import sys
from collections import deque

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
graph = {i: [] for i in range(1, n + 1)}
indeg = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    u, v = tuple(map(int, input().split()))
    graph[u].append(v)
    indeg[v] += 1

q = deque()

for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

res = []
while q:
    cur = q.popleft()
    res.append(cur)
    for next in graph[cur]:
        indeg[next] -= 1
        if indeg[next] == 0:
            q.append(next)

print(*res)
