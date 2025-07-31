import sys
import heapq

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))
s, y, x = tuple(map(int, input().split()))

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# visited = [[False] * n for i in range(n)]

pq = []
for i in range(n):
    for j in range(n):
        if maps[i][j] > 0:
            heapq.heappush(pq, (maps[i][j], i, j))


def spread():
    global pq

    new_v = []
    while pq:
        kind, y, x = heapq.heappop(pq)
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= n or maps[ny][nx] > 0:
                continue
            maps[ny][nx] = kind
            heapq.heappush(new_v, (kind, ny, nx))
    pq = new_v


for _ in range(s):
    spread()

print(maps[y - 1][x - 1])
