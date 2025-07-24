import sys
import heapq
input = sys.stdin.readline
from collections import deque

tn = int(input())

def get_order(docs, idx):
    d = deque()
    h = []

    for i in range(len(docs)):
        d.append(i)
        heapq.heappush(h, -docs[i])

    order = []

    while d:
        if -h[0] > docs[d[0]]:
            d.append(d.popleft())
        else:
            i = d.popleft()
            heapq.heappop(h)
            order.append(i)
            
    return order.index(idx) + 1

    
for _ in range(tn):
    n, m = tuple(map(int, input().split()))
    docs = tuple(map(int, input().split()))
    print(get_order(docs, m))

