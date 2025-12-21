import sys

input = sys.stdin.readline
d = input().strip()


rank = {"+": 0, "-": 0, "*": 1, "/": 1}


def make_post(expr):
    res = []
    stack = []
    for c in expr:
        if c.isalpha():  # 피연산자
            res.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                res.append(stack.pop())
            stack.pop()  # '(' 제거
        else:  # 연산자
            while stack and stack[-1] != "(" and rank[stack[-1]] >= rank[c]:
                res.append(stack.pop())
            stack.append(c)

    while stack:
        res.append(stack.pop())
    return "".join(res)


print(make_post(d))
