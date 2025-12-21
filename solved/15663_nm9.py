import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()


def dfs(
    selected,
    visited,
    depth=0,
):
    if depth == m:
        print(" ".join(selected))
        return

    last = None
    for i in range(0, n):
        if visited[i] or nums[i] == last:
            continue
        visited[i] = True
        selected.append(str(nums[i]))
        dfs(selected, visited, depth + 1)
        visited[i] = False
        selected.pop()
        last = nums[i]


dfs([], [False] * n)
