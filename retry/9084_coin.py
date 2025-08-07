import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)  # 금액별로 만드는 경우의수
    dp[0] = 1

    for coin in coins:
        for j in range(coin, m + 1):
            dp[j] += dp[j - coin]

    print(dp[m])
