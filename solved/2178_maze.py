# 최단거리문제
import sys
from collections import deque

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

maps = []
for _ in range(n):
    maps.append(list(map(int, input().strip())))

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    dist = maps[y][x]
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or nx >= m or ny >= n or maps[ny][nx] != 1:
            continue
        maps[ny][nx] = dist + 1
        q.append((ny, nx))


print(maps[n - 1][m - 1])
