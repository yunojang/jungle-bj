import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()


def dfs(selected, visited, depth=0):
    if depth == m:
        print(" ".join(selected))
        return

    for i in range(0, n):
        if visited[i]:
            continue
        selected.append(str(nums[i]))
        visited[i] = True
        dfs(selected, visited, depth + 1)
        selected.pop()
        visited[i] = False


visited = [False] * n

dfs([], visited)
