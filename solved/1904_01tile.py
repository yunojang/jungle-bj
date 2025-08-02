import sys

input = sys.stdin.readline
n = int(input())

m = [0] * 3
m[1], m[2] = 1, 2

for i in range(3, n + 1):
    t = m[1]
    m[1] = m[2]
    m[2] = (t + m[2]) % 15746

print(m[2] if n >= 2 else m[n])
