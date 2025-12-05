import sys

input = sys.stdin.readline
r, c = tuple(map(int, input().split()))
maps = [list(input().strip()) for _ in range(r)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(y, x, mask, cnt=1):
    best = cnt
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            continue
        bit = 1 << (ord(maps[ny][nx]) - 65)
        if mask & bit:
            continue
        best = max(best, dfs(ny, nx, mask | bit, cnt + 1))
    return best


start_mask = 1 << (ord(maps[0][0]) - 65)
print(dfs(0, 0, start_mask))
