import sys

input = sys.stdin.readline

n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
dp = [[0] * 2 for _ in range(n + 1)]

for step in range(1, n + 1):
    score = scores[step]

    dp[step][0] = max(dp[step - 2][0], dp[step - 2][1]) + score
    dp[step][1] = dp[step - 1][0] + score

print(max(dp[n]))
