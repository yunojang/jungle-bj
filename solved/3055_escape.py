# 확산 + 최단경로
# 물은 확산, 고슴도치 시작점으로, 물/벽 피해 목적지 최단경로
import sys
from collections import deque

input = sys.stdin.readline
n, m = tuple(list(map(int, input().split())))
s = None
d = None
maps = []
water = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    row = list(input().strip())
    maps.append(row)
    for j in range(m):
        if row[j] == "D":
            d = (i, j)
        if row[j] == "S":
            s = (i, j)
        if row[j] == "*":
            water.append((i, j))


def spread_water():
    global water
    new_water = []
    for y, x in water:
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            # 이전 물을 필터링 안하고 담아, 메모리 초과 문제!
            if maps[ny][nx] in "*DX":
                continue
            maps[ny][nx] = "*"
            new_water.append((ny, nx))
    water = new_water


hog = deque([s])
# maps[s[0]][s[1]] = 0
visited = [[0] * m for _ in range(n)]
cur_cycle = -1
while hog:
    cy, cx = hog.popleft()
    dist = visited[cy][cx]

    if cur_cycle < dist:
        spread_water()
        cur_cycle = dist

    for dy, dx in dirs:
        ny, nx = cy + dy, cx + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if visited[ny][nx] > 0 or maps[ny][nx] in "*X":
            continue
        visited[ny][nx] = dist + 1
        hog.append((ny, nx))

r = visited[d[0]][d[1]]
print(r if r > 0 else "KAKTUS")
