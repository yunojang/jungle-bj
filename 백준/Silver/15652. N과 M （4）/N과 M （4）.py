import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))


def dfs(nums=[], depth=0):
    if depth == m:
        print(*nums)
        return
    for i in range(nums[-1] if nums else 1, n + 1):
        dfs([*nums, i], depth + 1)


dfs()
