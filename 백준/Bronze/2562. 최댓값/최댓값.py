import sys

lines = sys.stdin.readlines()
nums = list(map(int, lines))

mv = 0
mi = None
for i in range(len(nums)):
    if nums[i] > mv:
        mv = nums[i]
        mi = i

print(mv)
print(mi + 1)
