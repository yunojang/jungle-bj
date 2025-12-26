import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
times = [int(input()) for _ in range(n)]


def get_allow(time):
    cnt = 0
    for t in times:
        cnt += time // t
    return cnt


def upper_bound(l, r):
    if l > r:
        return l

    mid = (l + r) // 2
    mid_allow = get_allow(mid)
    if mid_allow >= m:
        return upper_bound(l, mid - 1)
    else:
        return upper_bound(mid + 1, r)


print(upper_bound(1, max(times) * m))
