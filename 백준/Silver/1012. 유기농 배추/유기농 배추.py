import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input())

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def spread(maps, y, x, n, m):
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] == 0:
            continue
        maps[ny][nx] = 0
        spread(maps, ny, nx, n, m)


for _ in range(t):
    m, n, k = tuple(map(int, input().split()))
    maps = [[0] * m for _ in range(n)]
    # input
    for _ in range(k):
        x, y = tuple(map(int, input().split()))
        maps[y][x] = 1

    cnt = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 1:
                cnt += 1
                maps[y][x] = 0
                spread(maps, y, x, n, m)

    print(cnt)
