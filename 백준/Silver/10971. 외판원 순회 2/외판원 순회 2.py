import sys
from math import inf

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
best = inf
visited = [False] * n


def dfs(depth, cur, start, cost=0):
    global best
    if depth == n - 1:
        if maps[cur][start] > 0:
            best = min(best, cost + maps[cur][start])
        return

    for next in range(n):
        cur_cost = maps[cur][next]
        if visited[next] or next == start or cur_cost == 0 or cost + cur_cost > best:
            continue
        visited[next] = True
        dfs(depth + 1, next, start, cost + cur_cost)
        visited[next] = False


for start in range(n):
    visited[start] = True
    dfs(0, start, start)
    visited[start] = False

print(best)
