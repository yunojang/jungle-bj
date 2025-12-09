import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
keys = list(map(int, input().split()))

nums.sort()


def lower_bound(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2
    c = nums[mid]
    if target <= c:
        return lower_bound(start, mid, target)
    else:
        return lower_bound(mid + 1, end, target)


def upper_bound(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2
    c = nums[mid]
    if target < c:
        return upper_bound(start, mid, target)
    else:
        return upper_bound(mid + 1, end, target)


res = []

for key in keys:
    res.append(upper_bound(0, n, key) - lower_bound(0, n, key))

print(*res)
