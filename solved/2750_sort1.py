import sys

sys.setrecursionlimit(10**5)
inputs = sys.stdin.readlines()
n = int(inputs[0])
nums = list(map(int, map(str.strip, inputs[1:])))


def quick_ip(nums, start, end):
    if start >= end:
        return nums

    # pivot_idx = (start + end - 1) // 2
    # nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]
    pivot = nums[start]
    sp = start + 1

    for i in range(sp, end):
        if nums[i] < pivot:
            nums[i], nums[sp] = nums[sp], nums[i]
            sp += 1
    else:
        nums[start], nums[sp - 1] = nums[sp - 1], nums[start]

    quick_ip(nums, start, sp - 1)
    quick_ip(nums, sp, end)

    return nums


for v in quick_ip(nums, 0, len(nums)):
    print(v)
