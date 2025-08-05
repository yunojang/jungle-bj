import sys

input = sys.stdin.readline

n = int(input())
t = [0] * 2
t[0], t[1] = 0, 1

for _ in range(2, n + 1):
    f, s = t
    t[0] = s
    t[1] = (f % 1000000007 + s % 1000000007) % 1000000007

print(t[1] if n != 0 else 0)
