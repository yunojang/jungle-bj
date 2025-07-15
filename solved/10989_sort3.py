import sys

n = int(sys.stdin.readline())

# max_val = max(nums)
count = [0] * (10000 + 1)

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)
