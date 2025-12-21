import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

cnt = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == x:
#             cnt += 1

# print(cnt)
l = 0
r = n - 1
nums.sort()

while l < r:
    s = nums[l] + nums[r]
    if s == x:
        cnt += 1

    if s >= x:
        r -= 1
    else:
        l += 1

print(cnt)
