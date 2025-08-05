import sys

input = sys.stdin.readline

n = int(input())
confs = []

for _ in range(n):
    confs.append(tuple(map(int, input().split())))

cnt = 0
cur_end = 0

confs.sort(key=lambda t: (t[1], t[0]))

for s, e in confs:
    if cur_end <= s:
        cnt += 1
        cur_end = e

print(cnt)
