import sys

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]
dp[1][1] = nums[0]

for i in range(2, n + 1):
    cur = nums[i - 1]
    dp[i][1] = max(dp[i - 2]) + cur
    dp[i][2] = dp[i - 1][1] + cur

print(max(dp[n]))
