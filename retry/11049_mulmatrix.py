import sys

input = sys.stdin.readline

n = int(input())
ms = [tuple(map(int, input().split())) for _ in range(n)]
t = [[0] * (n + 1) for _ in range(n + 1)]

for diff in range(1, n):
    for i in range(1, n - diff + 1):
        j = i + diff
        t[i][j] = float("inf")
        for k in range(i, j):
            t[i][j] = min(
                t[i][j],
                (t[i][k] + t[k + 1][j] + ms[i - 1][0] * ms[k][0] * ms[j - 1][1]),
            )

print(t[1][n])
