import sys

n = int(sys.stdin.readline())
opers = list(map(lambda l: l.split(), sys.stdin.readlines()))

stack = []

for oper in opers:
    if oper[0] == "push":
        stack.append(oper[1])
    if oper[0] == "pop":
        print(stack.pop() if stack else -1)
    if oper[0] == "top":
        print(stack[-1] if stack else -1)
    if oper[0] == "size":
        print(len(stack))
    if oper[0] == "empty":
        print(0 if stack else 1)
