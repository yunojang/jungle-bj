import sys

input = sys.stdin.readline
t = int(input())

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(scores, n, y, x, visited, total=0):
    for y in range(2):
        for x in range(n):
            if visited[y][x]:
                continue
            # check
            visited[y][x] = True
            total += scores[y][x]
            for dy, dx in dirs:
                ny, nx = dy + y, dx + x
                if ny < 0 or nx < 0 or ny >= 2 or nx >= n or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
            dfs(scores, n, y, x, visited, total)
            # uncheck
            visited[y][x] = False
            total -= scores[y][x]
            for dy, dx in dirs:
                ny, nx = dy + y, dx + x
                if ny < 0 or nx < 0 or ny >= 2 or nx >= n:
                    continue
                visited[ny][nx] = False


for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    print(dfs(scores, n, 0, 0, [[False] * n for _ in range(2)]))
