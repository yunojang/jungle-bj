import sys

input = sys.stdin.readline

n = int(input())
a = "0" + input().strip()
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    s, e = tuple(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

total_route = 0
for i in range(1, n + 1):
    if a[i] == "0":
        continue
    visited = [False] * (n + 1)

    # cur 에서 나올수있는 경로 수 리턴
    def dfs(cur, first=False):
        if visited[cur] and a[cur] == "1":
            return 0
        visited[cur] = True

        if not first and a[cur] == "1":
            return 1
        else:
            cnt = 0
            for adj in graph[cur]:
                cnt += dfs(adj)
            return cnt

    total_route += dfs(i, True)

print(total_route)
