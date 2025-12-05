import sys

input = sys.stdin.readline
n = int(input())
count = [0] * 8001

sum_v = 0
min_v = 4000
max_v = -4000

for _ in range(n):
    num = int(input())
    sum_v += num
    min_v = min(min_v, num)
    max_v = max(max_v, num)
    count[num + 4000] += 1


print(round(sum_v / n))

cur = 0
freq = 0

target = n // 2 + 1
for i in range(8001):
    cnt = count[i]
    if not cnt:
        continue

    if cur < target <= cur + cnt:
        print(i - 4000)
    cur += cnt

freq = max(count)
modes = [i - 4000 for i, c in enumerate(count) if c == freq]
print(modes[1] if len(modes) > 1 else modes[0])


print(max_v - min_v)
