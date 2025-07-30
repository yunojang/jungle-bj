import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().strip())))

pass_black = [[None] * n for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque([(0, 0)])
pass_black[0][0] = 0
while q:
    y, x = q.popleft()
    passed = pass_black[y][x]

    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        np = passed + (1 if maps[ny][nx] == 0 else 0)
        if pass_black[ny][nx] is not None and pass_black[ny][nx] <= np:
            continue
        pass_black[ny][nx] = np
        q.append((ny, nx))

print(pass_black[n - 1][n - 1])
