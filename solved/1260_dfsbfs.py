import sys
from collections import deque

input = sys.stdin.readline
n, m, v = tuple(map(int, input().split()))

graph = {i: [] for i in range(1,n+1)}
for _ in range(m):
    s, e = tuple(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)



def dfs(graph, cur, visited):
    if cur in visited:
        return
    print(cur, end=" ")
    visited.add(cur)
    for adj in sorted(graph[cur]):
        dfs(graph, adj, visited)


def bfs(graph, start):
    q = deque([start])
    visited = set()
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        print(cur, end=' ')
        visited.add(cur)
        for adj in sorted(graph[cur]):
            if adj not in visited:
                q.append(adj)
    print()

dfs(graph, v, set())
print()
bfs(graph, v)