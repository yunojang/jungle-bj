# 다중 확산
import sys
from collections import deque

input = sys.stdin.readline
n, m, h = list(map(int, input().split()))
tomato = []
for _ in range(h):
    floor = []
    for _ in range(m):
        floor.append(list(map(int, input().split())))
    tomato.append(floor)

dirZ = [1, -1, 0, 0, 0, 0]
dirY = [0, 0, 1, -1, 0, 0]
dirX = [0, 0, 0, 0, 1, -1]

q = deque()
for z in range(h):
    for y in range(m):
        for x in range(n):
            if tomato[z][y][x] == 1:
                q.append((z, y, x))

while q:
    cz, cy, cx = q.popleft()
    day = tomato[cz][cy][cx]
    for i in range(6):
        dz, dy, dx = dirZ[i], dirY[i], dirX[i]
        nz, ny, nx = dz + cz, dy + cy, dx + cx
        if nz < 0 or ny < 0 or nx < 0 or nz >= h or ny >= m or nx >= n:
            continue
        if tomato[nz][ny][nx] != 0:
            continue
        tomato[nz][ny][nx] = day + 1
        q.append((nz, ny, nx))


def get_day():
    max_day = 0
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if tomato[z][y][x] == 0:
                    return -1
                max_day = max(max_day, tomato[z][y][x] - 1)
    return max_day


print(get_day())
