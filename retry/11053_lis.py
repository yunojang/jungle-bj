import sys

input = sys.stdin.readline

n = int(input())
ns = tuple(map(int, input().split()))
t = [0] * (n + 1)

for i in range(1, n + 1):
    max_cnt = 0
    for j in range(i):
        if ns[j - 1] < ns[i - 1]:
            max_cnt = max(max_cnt, t[j])
    t[i] = max_cnt + 1

print(max(t))
