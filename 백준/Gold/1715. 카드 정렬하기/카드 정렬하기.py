import sys
import heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

cnt = 0

while len(h) >= 2:
    min1 = heapq.heappop(h)
    min2 = heapq.heappop(h)
    s = min1 + min2

    cnt += s
    heapq.heappush(h, s)

print(cnt)
