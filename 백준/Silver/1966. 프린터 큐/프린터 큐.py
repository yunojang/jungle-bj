import sys
input = sys.stdin.readline
from collections import deque

tn = int(input())

def get_order(docs, idx):
    d = deque()

    for i in range(len(docs)):
        d.append(i)

    order = 1
    while d:
        if any([docs[idx] > docs[d[0]] for idx in d]):
            d.append(d.popleft())
        else:
            i = d.popleft()
            if i == idx:
                return order
            order += 1 

    
    
for _ in range(tn):
    n, m = tuple(map(int, input().split()))
    docs = tuple(map(int, input().split()))
    print(get_order(docs, m))

