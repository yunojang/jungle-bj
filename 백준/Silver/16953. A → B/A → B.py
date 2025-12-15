import sys

input = sys.stdin.readline
a, b = tuple(map(int, input().split()))


def c2(num):
    return int(str(num) + "1")


def dfs(cur, cnt=1):
    if cur == b:
        print(cnt)
        return True

    succ = False
    if cur * 2 <= b:
        succ |= dfs(cur * 2, cnt + 1)
    if c2(cur) <= b:
        succ |= dfs(c2(cur), cnt + 1)

    return succ


valid = dfs(a)
if not valid:
    print(-1)
