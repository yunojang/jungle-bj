import sys
from collections import deque

n = int(sys.stdin.readline())
opers = list(map(lambda l: tuple(l.split()), sys.stdin.readlines()))

q = deque()

for oper in opers:

    if oper[0] == "push":
        q.append(oper[1])
    if oper[0] == "pop":
        print(q.popleft() if q else -1)
    if oper[0] == "size":
        print(len(q))
    if oper[0] == "empty":
        print(0 if q else 1)
    if oper[0] == "front":
        print(q[0] if q else -1)
    if oper[0] == "back":
        print(q[-1] if q else -1)
