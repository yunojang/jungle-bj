import sys

input = sys.stdin.readline
N, r, c = list(map(int, input().split()))


def z_order(n, y, x, offset):
    if n == 0:
        return offset

    half = 1 << (n - 1)
    q_size = half**2

    quad = 0
    if r >= y + half:
        quad += 2
        y += half
    if c >= x + half:
        quad += 1
        x += half

    offset += quad * q_size
    return z_order(n - 1, y, x, offset)


print(z_order(N, 0, 0, 0))
