import sys

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or maps[i][j] == 0:
            continue
        d = maps[i][j]
        if i + d < n:
            dp[i + d][j] += dp[i][j]
        if j + d < n:
            dp[i][j + d] += dp[i][j]

print(dp[n - 1][n - 1])
