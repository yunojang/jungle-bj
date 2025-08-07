import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")
dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0  # visited - 1 cur-0으로 시작

for visited in range(1, 1 << n):
    for cur in range(n):
        if not visited & (1 << cur):
            continue
        for next in range(n):
            if cur == next or visited & (1 << next) or graph[cur][next] == 0:
                continue
            next_visited = visited | (1 << next)
            dp[next_visited][next] = min(
                dp[next_visited][next], dp[visited][cur] + graph[cur][next]
            )

res = INF
for end_cur in range(n):
    if graph[end_cur][0] == 0:
        continue
    cost = dp[(1 << n) - 1][end_cur] + graph[end_cur][0]
    res = min(res, cost)

print(res)
