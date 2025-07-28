import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    s,e  = tuple(map(int,input().split()))
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)

def visite(cur):
    cnt = 0
    if visited[cur]:
        return 0
    visited[cur] = True
    cnt += 1
    for adj in graph[cur]:
        cnt += visite(adj)
    return cnt

print(visite(1) -1) # 1로부터 감염되는 다른 정점이라 -1