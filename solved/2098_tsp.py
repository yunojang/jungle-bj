import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = float("inf")
cost = [[INF] * n for _ in range(1 << n)]
cost[1][0] = 0

for visited in range(1, 1 << n):
    for cur in range(n):
        if not (visited & (1 << cur)):
            continue
        for next in range(n):
            if visited & (1 << next) or graph[cur][next] == 0:
                continue
            next_visited = visited | (1 << next)
            cost[next_visited][next] = min(
                cost[next_visited][next], cost[visited][cur] + graph[cur][next]
            )

ans = INF
for i in range(n):
    if graph[i][0] == 0:
        continue
    all_visited = (1 << n) - 1
    ans = min(ans, cost[all_visited][i] + graph[i][0])

print(ans)
