import sys
n = int(sys.stdin.readline())
import heapq

h = [] 
for _ in range(n):
    oper = int(sys.stdin.readline())
    if oper == 0:
        print(heapq.heappop(h)[1] if h else 0)
    else:
        heapq.heappush(h, (abs(oper), oper))