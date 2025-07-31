import sys

input = sys.stdin.readline

n = int(input())
maps = []

for _ in range(n):
    maps.append(list(input().strip()))

cnts = []
visited = [[False] * n for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 현재 집에서 이어진 집의 개수를 반환
def chk_house(y, x):
    cnt = 1
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= n or maps[ny][nx] == "0":
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        cnt += chk_house(ny, nx)
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == "1":
            visited[i][j] = True
            cnts.append(chk_house(i, j))

print(len(cnts))
for cnt in sorted(cnts):
    print(cnt)
