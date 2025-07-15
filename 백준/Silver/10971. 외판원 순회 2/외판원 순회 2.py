import sys

n = int(sys.stdin.readline())

costs = []

for i in range(n):
    costs.append(list(map(int, sys.stdin.readline().split(" "))))

min_cost = [float("inf")]


def search(path, cur=None, t_cost=0):
    if len(path) == n + 1:
        min_cost[0] = min(t_cost, min_cost[0])

    is_last = len(path) == n
    for i in range(n):
        cost = costs[cur][i] if cur is not None else -1

        if cost == 0:
            continue

        if is_last and i != path[0]:
            continue

        if not is_last and i in path:
            continue

        search(path + [i], i, t_cost + max(cost, 0))


search([])
print(min_cost[0])
