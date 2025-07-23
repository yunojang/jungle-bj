import sys
import heapq

n = int(sys.stdin.readline())
roads = []

for _ in range(n):
    roads.append(sorted(tuple(map(int, sys.stdin.readline().split()))))

d = int(sys.stdin.readline())

roads.sort(key=lambda r:r[1])
# n^2 탐색 -> 예제 완료(시간초과)
# 슬라이딩 윈도우 -> N

h = []
max_cnt = 0
for s, e in roads:
    heapq.heappush(h,s)

    while h and (h[0] < e-d):
        heapq.heappop(h)

    max_cnt = max(max_cnt, len(h))

print(max_cnt)