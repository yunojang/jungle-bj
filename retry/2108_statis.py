import sys

input = sys.stdin.readline

n = int(input())
count = [0] * 8001
sum = 0
min_v = 4000
max_v = -4000

for i in range(n):
    num = int(input())
    count[num + 4000] += 1
    sum += num
    min_v = min(min_v, num)
    max_v = max(max_v, num)

print(round(sum / n))

cur = 0
for i in range(8001):
    c = count[i]
    if not c:
        continue
    if cur < (n // 2 + 1) <= cur + c:
        print(i - 4000)
    cur += c

freq = max(count)
modes = [i - 4000 for i, c in enumerate(count) if c == freq]
print(modes[1] if len(modes) > 1 else modes[0])

print(max_v - min_v)
