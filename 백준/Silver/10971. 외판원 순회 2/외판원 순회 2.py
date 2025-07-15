import sys

n = int(sys.stdin.readline())

costs = []

for i in range(n):
    costs.append(list(map(int, sys.stdin.readline().split(" "))))

min_cost = [float("inf")]


def search(path, visited, cur=None, t_cost=0):
    if len(path) == n:
        back_cost = costs[cur][path[0]]

        if back_cost == 0:
            return

        min_cost[0] = min(t_cost + back_cost, min_cost[0])

    for i in range(n):
        cost = costs[cur][i] if cur is not None else -1

        if i in visited or cost == 0:
            continue

        visited.add(i)
        search(path + [i], visited, i, t_cost + max(cost, 0))
        visited.remove(i)


search([], set())
print(min_cost[0])
