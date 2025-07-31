import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))

maps = []
for _ in range(n):
    maps.append(list(input().strip()))
visited = [[False] * m for _ in range(n)]
cnt = 0

vd = [(1, 0), (-1, 0)]
hd = [(0, 1), (0, -1)]


def check_same(y, x):
    dirs = vd if maps[y][x] == "|" else hd

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if maps[ny][nx] != maps[y][x] or visited[ny][nx]:
            continue
        visited[ny][nx] = True
        check_same(ny, nx)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += 1
            check_same(i, j)
            visited[i][j] = True

print(cnt)
