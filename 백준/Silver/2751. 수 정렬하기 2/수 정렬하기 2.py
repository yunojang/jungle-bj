import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
nums = list(map(int, map(str.strip, inputs[1:])))

# count = [0] * 1000000
# count

nums.sort()
for n in nums:
    print(n)
