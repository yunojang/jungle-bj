import heapq
import sys

h = []
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))

for i in range(n):
    heapq.heappush(h, nums[i])
    mid = i // 2  # 이 인덱스와 같은레벨
    print(mid, h)
