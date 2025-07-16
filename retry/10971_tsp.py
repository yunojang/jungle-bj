import sys

n = int(sys.stdin.readline())
costs = []

for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().split(" "))))


min_cost = float("inf")


def move(path, cur=None, cost=0):
    global min_cost
    if len(path) == n:
        back_cost = costs[cur][path[0]]
        if back_cost == 0:
            return

        min_cost = min(min_cost, cost + back_cost)
        return

    for i in range(n):
        # 제약조건
        is_block = cur is not None and costs[cur][i] == 0
        # 효율 - 백트래킹
        new_cost = cost + (costs[cur][i] if cur is not None else 0)
        is_over_cost = new_cost > min_cost

        if i in path or is_block or is_over_cost:
            continue

        move(path + [i], i, new_cost)


move([])
print(min_cost)
