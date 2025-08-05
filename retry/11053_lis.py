import sys

input = sys.stdin.readline
n = int(input())
ns = list(map(int, input().split()))

t = [0] * (n + 1)

for i in range(n):
    m = 0
    for j in range(i):
        if ns[i] > ns[j]:
            m = max(m, t[j])
    t[i] = m + 1

print(max(t))
