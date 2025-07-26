import sys
from collections import deque, defaultdict

n, m = tuple(map(int,sys.stdin.readline().split()))
edges = list(map(lambda l: tuple(map(int, l.split())), sys.stdin.readlines()))

graph = defaultdict(list)
indegree = [0] * (n+1)
q = deque()
res = []

for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

for _ in range(n):
    x = q.popleft()
    res.append(x)
    for v in graph[x]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print(*res)