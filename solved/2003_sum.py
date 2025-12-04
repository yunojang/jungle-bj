import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0
start = end = 0
cur = 0

while True:
    if cur >= m:
        if cur == m:
            cnt += 1
        cur -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        cur += nums[end]
        end += 1

print(cnt)
