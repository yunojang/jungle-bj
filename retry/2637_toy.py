import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n + 1)}
indeg = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
    v, u, c = tuple(map(int, input().split()))
    graph[u].append((v, c))
    indeg[v] += 1

ms = [[0] * (n + 1) for _ in range(n + 1)]
q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)
        ms[i][i] = 1

while q:
    cur = q.popleft()
    for next, cnt in graph[cur]:
        for i in range(1, n + 1):
            ms[next][i] += ms[cur][i] * cnt
        indeg[next] -= 1
        if indeg[next] == 0:
            q.append(next)

for i in range(1, n + 1):
    if ms[n][i]:
        print(i, ms[n][i])
