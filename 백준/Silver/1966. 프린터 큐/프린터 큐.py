import sys
import heapq
input = sys.stdin.readline
from collections import deque

tn = int(input())

def get_order(docs, idx):
    q = deque()
    h = []

    for i in range(len(docs)):
        q.append(i)
        heapq.heappush(h, -docs[i])

    # order = []
    cnt = 1
    while q:
        if -h[0] > docs[q[0]]:
            q.append(q.popleft())
        else:
            i = q.popleft()
            heapq.heappop(h)
            if idx == i:
                return cnt
            cnt+=1
    #         order.append(i)
    # return order.index(idx) + 1

    
for _ in range(tn):
    n, m = tuple(map(int, input().split()))
    docs = tuple(map(int, input().split()))
    print(get_order(docs, m))

