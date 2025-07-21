import sys

n = int(sys.stdin.readline())


def is_valid(line):
    stack = []
    for c in line:
        if c == ")":
            if not stack or stack.pop() != "(":
                return False
        else:
            stack.append(c)
    return len(stack) == 0


lines = []
for i in range(n):
    lines.append(sys.stdin.readline()[:-1])

for line in lines:
    print("YES" if is_valid(line) else "NO")
