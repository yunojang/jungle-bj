import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(n)]

best = 0
cnt = 0

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def inj(maps, y, x):
    size = 1
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] == 0:
            continue
        maps[ny][nx] = 0
        size += inj(maps, ny, nx)
    return size


for y in range(n):
    for x in range(m):
        if maps[y][x] == 1:
            cnt += 1
            maps[y][x] = 0
            best = max(best, inj(maps, y, x))

print(cnt)
print(best)
