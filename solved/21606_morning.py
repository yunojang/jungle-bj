import sys
from collections import deque

# sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
a = [None] + list(map(int, input().strip()))
graph = {i: [] for i in range(1, n + 1)}
edges = []

for _ in range(n - 1):
    s, e = tuple(map(int, input().split()))
    edges.append((s, e))
    graph[s].append(e)
    graph[e].append(s)

total_route = 0
for u, v in edges:
    if a[u] == 1 and a[v] == 1:
        total_route += 2

visited = [False] * (n + 1)
for i in range(1, n + 1):
    if a[i] == 0 and not visited[i]:
        q = deque([i])
        visited[i] = True
        in_set = set()

        while q:
            x = q.popleft()
            for adj in graph[x]:
                if a[adj] == 0 and not visited[adj]:
                    visited[adj] = True
                    q.append(adj)
                elif a[adj] == 1:
                    in_set.add(adj)

        k = len(in_set)
        total_route += k * (k - 1)

print(total_route)


# for i in range(1, n + 1):
#     if a[i] == 0:
#         continue
#     visited = [False] * (n + 1)

#     # cur 에서 나올수있는 경로 수 리턴
#     def dfs(cur, first=False):
#         if visited[cur]:
#             return 0
#         visited[cur] = True
#         if not first and a[cur] == 1:
#             return 1
#         cnt = 0
#         for adj in graph[cur]:
#             cnt += dfs(adj)
#         return cnt

#     cnt = dfs(i, True)
#     # print("@", i, cnt)
#     total_route += cnt

# print(total_route)
