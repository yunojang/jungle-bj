import sys

nums = list(map(int, sys.stdin.readlines()))
m = 1
for num in nums:
    m *= num

counts = [0] * 10
for c in str(m):
    counts[int(c)] += 1

for c in counts:
    print(c)
