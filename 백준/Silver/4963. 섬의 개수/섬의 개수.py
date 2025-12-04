import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]


def fill(maps, y, x):
    w, h = len(maps[0]), len(maps)
    maps[y][x] = 0  # land -> sea
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= h or nx >= w or maps[ny][nx] == 0:
            continue
        fill(maps, ny, nx)


def cnt_land(maps, w, h):
    cnt = 0
    for y in range(h):
        for x in range(w):
            if maps[y][x] == 0:
                continue
            else:
                cnt += 1
                fill(maps, y, x)
    return cnt


while True:
    w, h = tuple(map(int, input().split()))
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    print(cnt_land(maps, w, h))
