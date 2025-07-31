import sys

input = sys.stdin.readline
n = int(input())
m = [None] * max(2, n + 1)
m[0], m[1] = 0, 1

for i in range(2, n + 1):
    m[i] = m[i - 1] + m[i - 2]

print(m[n])
