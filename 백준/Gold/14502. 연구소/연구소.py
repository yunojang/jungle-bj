import sys
from itertools import combinations

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(n)]


def get_safe(maps):
    return sum(row.count(0) for row in maps)


dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def spread(maps, y, x):
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] != 0:
            continue
        maps[ny][nx] = 2
        spread(maps, ny, nx)


best_sz = 0


def count(maps):
    global best_sz

    for y in range(n):
        for x in range(m):
            if maps[y][x] == 2:
                spread(maps, y, x)
    best_sz = max(best_sz, get_safe(maps))


empties = [(y, x) for y in range(n) for x in range(m) if maps[y][x] == 0]

for walls in combinations(empties, 3):
    tmp = [row[:] for row in maps]
    for y, x in walls:
        tmp[y][x] = 1
    count(tmp)

print(best_sz)
