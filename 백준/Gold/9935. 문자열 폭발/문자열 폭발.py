import sys
input = sys.stdin.readline

s = str(input())[0:-1]
explode_s = str(input())[0:-1]
explode_l = len(explode_s)

stack = []

for c in s:
    stack.append(c)
    while stack and ("".join(stack[len(stack)-explode_l:]) == explode_s):
        for _ in range(explode_l):
            stack.pop()

print("".join(stack) if stack else "FRULA")