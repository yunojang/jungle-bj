import sys

lines = sys.stdin.readlines()
n = int(lines[0])
nums = list(map(lambda l: tuple(map(int, l.split(" "))), lines[1:]))

for a, b in nums:
    print(a + b)
