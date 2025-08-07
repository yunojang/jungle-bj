import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
banned = set([int(input()) for _ in range(m)])

max_k = int((2 * n) ** 0.5)
INF = float("inf")
dp = [[INF] * (max_k + 1) for _ in range(n + 1)]
dp[1][0] = 0

for i in range(1, n + 1):
    for j in range(max_k + 1):
        if dp[i][j] == INF:
            continue
        for nj in (j - 1, j, j + 1):
            np = i + nj
            if nj < 1 or np in banned or np > n:
                continue
            dp[np][nj] = min(dp[np][nj], dp[i][j] + 1)

res = min(dp[n])
print(res if res != INF else -1)
