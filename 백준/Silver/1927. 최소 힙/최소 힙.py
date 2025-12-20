import sys
import heapq

input = sys.stdin.readline
n = int(input())
hq = []

for _ in range(n):
    oper = int(input())
    if oper == 0:
        print(heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, oper)
