import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))

stack = []
for n in nums:
    while stack and stack[-1] <= n:
        stack.pop()
    stack.append(n)

print(len(stack))
