import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    t = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        coin = coins[i - 1]
        for j in range(1, m + 1):
            if coin > j:
                t[i][j] = t[i - 1][j]
            else:
                for k in range(j // coin + 1):
                    t[i][j] += t[i - 1][j - (k * coin)]
                if j % coin == 0:
                    t[i][j] += 1

    print(t[n][m])
