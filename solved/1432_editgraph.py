import sys, heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
outdeg = [0] * (n+1)
for i in range(1, n+1):
    line = input().strip()
    for j, ch in enumerate(line, start=1):
        if ch == '1':
            graph[j].append(i) # j를 해결하는데 필요한 값 배열
            outdeg[i] += 1 # outdeg

orders = [0] * (n+1)
h = []
for i in range(1, n+1):
    if outdeg[i] == 0:
        heapq.heappush(h, -i) # max heap

cur = n
cnt = 0
while h:
    u = -heapq.heappop(h)
    orders[u] = cur
    cur -= 1
    cnt += 1
    for v in graph[u]:
        outdeg[v] -= 1
        if outdeg[v] == 0:
            heapq.heappush(h, -v)

if cnt < n:
    print(-1)
else:
    print(*orders[1:])
