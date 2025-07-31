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
    if maps[y][x] == "|":
        for dy, dx in vd:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or maps[ny][nx] == "-" or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            check_same(ny, nx)
    else:
        for dy, dx in hd:
            ny, nx = y + dy, x + dx
            if nx < 0 or nx >= m or maps[ny][nx] == "|" or visited[ny][nx]:
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
