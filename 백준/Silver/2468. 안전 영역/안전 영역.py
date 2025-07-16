import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
maps = []

max_height = 1
min_height = 100

for _ in range(n):
    line = []
    for v in list(map(int, sys.stdin.readline().split(" "))):
        max_height = max(v, max_height)
        min_height = min(v, min_height)
        line.append(v)
    maps.append(line)

# 다 안잠겼을때 => 1 (최소는 1)
max_area = 1

adjs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for cur_h in range(min_height, max_height):
    # 안전공간 개수 찾기
    safe_area = 0
    safe_map = [[h > cur_h for h in row] for row in maps]

    def adj_safe_remove(y, x):
        for dy, dx in adjs:
            ny = dy + y
            nx = dx + x
            if ny < 0 or nx < 0 or ny >= n or nx >= n or safe_map[ny][nx] == False:
                continue
            safe_map[ny][nx] = False
            adj_safe_remove(ny, nx)

    for y in range(n):
        for x in range(n):
            if safe_map[y][x]:
                safe_area += 1
                safe_map[y][x] = False
                adj_safe_remove(y, x)

    max_area = max(safe_area, max_area)


print(max_area)
