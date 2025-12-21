import sys

input = sys.stdin.readline
n = int(input())

s = set()

for _ in range(n):
    command = input().strip()
    oper, num = None, None
    if " " in command:
        oper, num = tuple(command.split())
        num = int(num)
    else:
        oper = command

    if oper == "add":
        s.add(num)
    elif oper == "check":
        print(1 if num in s else 0)
    elif oper == "remove":
        if num in s:
            s.remove(num)
    elif oper == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif oper == "all":
        s = set([i + 1 for i in range(20)])
    else:  # empty
        s = set()
