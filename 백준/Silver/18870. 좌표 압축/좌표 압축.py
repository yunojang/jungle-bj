import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
sn = sorted(nums)

pos = {}
cur = 0

for v in sn:
    if v not in pos:
        pos[v] = cur
        cur += 1

print(" ".join(map(str, [pos[x] for x in nums])))
