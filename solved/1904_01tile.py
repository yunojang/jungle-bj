import sys

input = sys.stdin.readline
n = int(input())
m = [None] * (n + 1)
m[1], m[2] = 1, 2

for i in range(3, n + 1):
    m[i] = ((m[i - 1] % 15746) * 2 - 1) % 15746

print(m[n] % 15746)
