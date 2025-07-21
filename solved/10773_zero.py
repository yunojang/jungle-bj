import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))

stack = []
for num in nums:
    if num == 0:
        stack.pop()
    else:
        stack.append(num)


print(sum(stack))
