from time import time

n, r, c = tuple(map(int, input().split(" ")))

visited = []
# cnt = [0]
ords = [(0, 0), (0, 1), (1, 0), (1, 1)]


def search(n, sy=0, sx=0, cnt=0):
    if n == 0:
        # visited.append((sy, sx))
        if sy == r and sx == c:
            print(cnt)
            return
            # print(cnt[0])
        # cnt[0] += 1
        return

    # z 순서로 재귀
    for i, (dy, dx) in enumerate(ords):
        unit = 2 ** (n - 1)
        ny, nx = (sy + dy * unit, sx + dx * unit)
        # ny,nx로 시작하는 공간 범위가 r,c를 포함하지 않으면 푸루닝
        if ny <= r and nx <= c and ny + unit > r and nx + unit > c:
            search(n - 1, ny, nx, cnt + (unit**2 * i))


# prev = time()
search(n)
# print(time() - prev)
# print(visited)
