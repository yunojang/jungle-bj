import sys, heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
outdeg = [0] * (n+1)
for i in range(1, n+1):
    row = input().strip()
    for j, ch in enumerate(row, start=1):
        if ch == '1':
            graph[j].append(i)
            outdeg[i] += 1

ans = [0] * (n+1)
heap = []
for i in range(1, n+1):
    if outdeg[i] == 0:
        heapq.heappush(heap, -i)

cur = n
cnt = 0
while heap:
    u = -heapq.heappop(heap)
    ans[u] = cur
    cur -= 1
    cnt += 1
    for v in graph[u]:
        outdeg[v] -= 1
        if outdeg[v] == 0:
            heapq.heappush(heap, -v)

if cnt < n:
    print(-1)
else:
    print(*ans[1:])
