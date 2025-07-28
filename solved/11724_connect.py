import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = tuple(map(int, input().split()))
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = tuple(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = set()

def visite(node):
    visited.add(node)
    for adj in graph[node]:
        if adj not in visited:
            visited.add(adj)
            visite(adj)

for node in graph.keys():
    if node not in visited:
        cnt += 1
        visite(node)
print(cnt)