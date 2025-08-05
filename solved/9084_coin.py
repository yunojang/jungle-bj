import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())

    table = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        coin = coins[i - 1]
        for j in range(1, k + 1):
            if coin > k:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] += table[i - 1][j]
                for x in range(1, (j // coin) + 1):
                    table[i][j] += table[i - 1][j - coin * x]
                if j % coin == 0:
                    table[i][j] += 1

    cnt = table[n][k]
    print(cnt)
