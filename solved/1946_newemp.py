import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    emp = []
    for _ in range(n):
        emp.append(tuple(map(int, input().split())))

    emp.sort()
    min_s = float("inf")
    cnt = 0
    for f, s in emp:
        if min_s > s:
            cnt += 1
            min_s = s
    print(cnt)
