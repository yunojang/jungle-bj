import sys

input = sys.stdin.readline

n = int(input())
ms = []

for _ in range(n):
    ms.append(tuple(map(int, input().split())))

t = [[0] * (n + 1) for _ in range(n + 1)]

for diff in range(1, n):
    for i in range(1, n - diff + 1):
        j = diff + i
        r = float("inf")
        for k in range(i, j):
            r = min(
                r, t[i][k] + t[k + 1][j] + ms[i - 1][0] * ms[k - 1][1] * ms[j - 1][1]
            )
        t[i][j] = r

print(t[1][n])
