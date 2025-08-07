import sys

input = sys.stdin.readline

n = int(input())

t = [1, 2]
for i in range(3, n + 1):
    t[0], t[1] = t[1], (t[0] + t[1]) % 15746

print(t[1] if n > 1 else t[0])
