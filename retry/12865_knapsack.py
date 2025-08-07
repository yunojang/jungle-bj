import sys

input = sys.stdin.readline
n, k = tuple(map(int, input().split()))
items = [tuple(map(int, input().split())) for _ in range(n)]

t = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i - 1]
    for j in range(1, k + 1):
        if w > j:
            t[i][j] = t[i - 1][j]
        else:
            t[i][j] = max(t[i - 1][j], v + t[i - 1][j - w])

print(t[n][k])
