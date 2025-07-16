import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
maps = []

max_h = 1
min_h = float("inf")

for row in range(n):
    row = []
    for v in list(map(int, sys.stdin.readline().split())):
        max_h = max(max_h, v)
        min_h = min(min_h, v)
        row.append(v)
    maps.append(row)

adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

max_safe_cnt = 1  # 하나도 안잠길때 1
for cur_h in range(min_h, max_h):
    count = 0
    safe_map = [[h > cur_h for h in row] for row in maps]

    def adj_chk(y, x):
        for dy, dx in adjs:
            ny, nx = dy + y, dx + x
            if ny < 0 or nx < 0 or nx >= n or ny >= n or not safe_map[ny][nx]:
                continue
            safe_map[ny][nx] = False
            adj_chk(ny, nx)

    for y in range(n):
        for x in range(n):
            if safe_map[y][x]:
                count += 1
                safe_map[y][x] = False
                adj_chk(y, x)

    max_safe_cnt = max(max_safe_cnt, count)


print(max_safe_cnt)
