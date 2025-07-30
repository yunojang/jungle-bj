import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))


def operate(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        if a < 0:
            return -(-a // b)
        return a // b


min_t = [float("inf")]
max_t = [float("-inf")]


def dfs(t, num_idx):
    if num_idx == n:
        max_t[0] = max(max_t[0], t)
        min_t[0] = min(min_t[0], t)
        return
    for op in range(4):
        if opers[op] == 0:
            continue
        opers[op] -= 1
        dfs(operate(t, nums[num_idx], op), num_idx + 1)
        opers[op] += 1


dfs(nums[0], 1)
print(max_t[0])
print(min_t[0])
