import heapq
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))
min_h = []
max_h = [-nums[0]]
print(nums[0])

for num in nums[1:]:
    if -max_h[0] > num:
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if len(max_h) < len(min_h):
        heapq.heappush(max_h, -heapq.heappop(min_h))
    
    if len(max_h) > len(min_h) + 1:
        heapq.heappush(min_h, -heapq.heappop(max_h))

    print(-max_h[0])

