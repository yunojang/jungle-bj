n, r, c = list(map(int, input().split(" ")))

orders = [(0, 0), (0, 1), (1, 0), (1, 1)]

count = 0


def search(n, y, x):
    global count

    if y == r and x == c:
        print(count)
        return True
    if n == 0:
        count += 1  # n이 0이 되어, 1개의 값을 검색하는 시점에서
        return False

    for dy, dx in orders:
        unit = 2 ** (n - 1)
        ny, nx = y + dy * unit, x + dx * unit

        if ny > r or nx > c or ny + unit <= r or nx + unit <= c:
            count += unit * unit
            continue

        if search(n - 1, ny, nx):
            return True


search(n, 0, 0)
