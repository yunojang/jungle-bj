n = int(input())
nums = list(map(int, input().split()))

nums.sort()

l = 0
r = n - 1

min_abs = float("inf")
min_nums = None

while l < r:
    sum = nums[l] + nums[r]
    if min_abs > abs(sum):
        min_abs = abs(sum)
        min_nums = (nums[l], nums[r])

    if sum > 0:
        r -= 1
    else:
        l += 1

a, b = min_nums
print(a, b)
