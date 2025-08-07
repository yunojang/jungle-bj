import sys

input = sys.stdin.readline
n = int(input())
money = (2, 5)
t = [0] * (max(n, 5) + 1)
t[2], t[4], t[5] = 1, 2, 1

for i in range(6, n + 1):
    if t[i - 2] == 0 and t[i - 5] == 0:
        continue

    if t[i - 2] == 0:
        t[i] = t[i - 5] + 1
    elif t[i - 5] == 0:
        t[i] = t[i - 2] + 1
    else:
        t[i] = min(t[i - 2], t[i - 5]) + 1

print(t[n] if t[n] != 0 else -1)
