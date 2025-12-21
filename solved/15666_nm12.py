import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()


def dfs(selected, visited, depth=0):
    if depth == m:
        print(" ".join(map(lambda i: str(nums[i]), selected)))
        return

    last = None
    for i in range(selected[-1] if selected else 0, n):
        if last == nums[i]:
            continue
        visited[i] = True
        selected.append(i)
        dfs(selected, visited, depth + 1)
        visited[i] = False
        selected.pop()
        last = nums[i]


dfs([], [False] * n)
