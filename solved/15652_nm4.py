import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))


def dfs(nums, depth=0):
    if depth == m:
        print(*nums)
        return
    for i in range(nums[-1] if nums else 1, n + 1):
        nums.append(i)
        dfs(nums, depth + 1)
        nums.pop()


dfs([])
