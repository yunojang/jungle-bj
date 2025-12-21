import sys
import heapq

input = sys.stdin.readline
n = int(input())

hq = []

for _ in range(n):
    oper = int(input())
    if oper == 0:
        _, payload = heapq.heappop(hq) if hq else (0, 0)
        print(payload)
    else:
        heapq.heappush(hq, (abs(oper), oper))
