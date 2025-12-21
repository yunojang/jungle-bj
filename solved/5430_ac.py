from collections import deque
import sys

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    p = input().strip()
    n = int(input())
    s = input().strip()[1:-1]
    isR = False
    nums = s.split(",") if s else []
    dq = deque(nums)

    for oper in p:
        if oper == "R":
            isR = not isR
        elif oper == "D":
            if len(dq):
                if isR:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print("error")
                dq = "error"
                break
    if dq != "error":
        if isR:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
