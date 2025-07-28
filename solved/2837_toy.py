import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
need = [[0] * (n+1) for _ in range(n+1)]


for _ in range(m):
    p, r, c = tuple(map(int, input().split()))
    graph[r].append((p, c))
    # graph[u].append(v)
    indegree[p] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        need[i][i] = 1

while q:
    cur = q.popleft() # 차수 0
    # 위상정렬 - 나를 조건으로 하는 모든 정점 대해 처리하고 차수 낮춤
    for next, cnt in graph[cur]:
        for i in range(1,n+1):
            # next 부품은 i를 만드는데 cur에 필요한i에 cnt배 필요 
            need[next][i] += need[cur][i] * cnt
        # cur 만드는데 필요한 모든 기본부품 카운트를 추가하고, 차수 낮춤
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in range(n):
    if need[n][i] > 0:
        print(i, need[n][i])