import sys
from collections import deque

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def melt():
    cnt = 0
    visited = [[maps[y][x] == 0 for x in range(m)] for y in range(n)]
    melted = [[0] * m for _ in range(n)]

    def visite(y, x):
        q = deque([(y, x)])
        while q:
            cy, cx = q.popleft()
            if cy < 0 or cx < 0 or cy >= n or cx >= m or visited[cy][cx]:
                continue
            visited[cy][cx] = True

            for dy, dx in dirs:
                ny, nx = dy + cy, dx + cx
                if maps[ny][nx] == 0:
                    melted[cy][cx] += 1
                else:
                    q.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                cnt += 1
                visite(i, j)
    for i in range(n):
        for j in range(m):
            maps[i][j] = max(0, maps[i][j] - melted[i][j])
    return cnt


time = 0
cnt = None
while (cnt := melt()) == 1:
    time += 1

print(time if cnt > 1 else 0)
