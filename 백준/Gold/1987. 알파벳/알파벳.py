import sys

input = sys.stdin.readline

r, c = tuple(map(int, input().split()))
maps = [list(input().strip()) for _ in range(r)]

best = 0


dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(y, x, visited="", cnt=1):
    global best
    best = max(best, cnt)
    visited += maps[y][x]
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= r or nx >= c or maps[ny][nx] in visited:
            continue
        dfs(ny, nx, visited, cnt + 1)


dfs(0, 0)

print(best)
