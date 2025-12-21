import sys
import math

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

diff_min = math.inf
diff_l, diff_r = None, None

l = 0
r = n - 1

while l < r:
    s = nums[l] + nums[r]
    if abs(diff_min) > abs(s):
        diff_min = s
        diff_l, diff_r = l, r

    if s >= 0:
        r -= 1
    else:
        l += 1

print(nums[diff_l], nums[diff_r])
