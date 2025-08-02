import sys

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
items = []

for _ in range(n):
    items.append(tuple(map(int, input().split())))

t = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, p = items[i - 1]
    for j in range(1, k + 1):
        if w > j:
            t[i][j] = t[i - 1][j]
        else:
            t[i][j] = max(t[i - 1][j], p + t[i - 1][j - w])

print(t[n][k])
