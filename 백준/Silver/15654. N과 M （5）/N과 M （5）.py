import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()


def dfs(selected, depth=0):
    if depth == m:
        print(" ".join(map(lambda i: str(nums[i]), selected)))
        return

    for i in range(0, n):
        if i in selected:
            continue
        selected.append(i)
        dfs(selected, depth + 1)
        selected.pop()


dfs([])
