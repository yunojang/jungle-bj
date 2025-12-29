import sys

input = sys.stdin.readline
m, n = tuple(map(int, input().split()))
snacks = list(map(int, input().split()))


def get_allow_man(snack_len):
    man = 0
    for x in snacks:
        man += x // snack_len
    return man


def upper_bound(l, r):
    if l > r:
        return l
    mid = (l + r) // 2
    mid_allow = get_allow_man(mid)

    if mid_allow >= m:
        return upper_bound(mid + 1, r)
    else:
        return upper_bound(l, mid - 1)


print(upper_bound(1, max(snacks)) - 1)
