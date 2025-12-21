import sys

n, m = list(map(int, sys.stdin.readline().split(" ")))
trees = list(map(int, sys.stdin.readline().split(" ")))

trees.sort()
max = trees[len(trees) - 1]


# s~e 사이의 높이 중, arr의 over_sum 값이 over_total보다 큰 최대 높이를 반환
def total_under_bound(arr, over_total, s=0, e=max):
    if s >= e:
        return s

    mid = (s + e) // 2
    if get_over_sum(arr, mid) >= over_total:
        return total_under_bound(arr, over_total, mid + 1, e)
    else:
        return total_under_bound(arr, over_total, s, mid)


# 배열 내 s~e에서 v를 초과하는 첫 값의 위치를 반환 (over_bound)
def over_bound(arr, v, s, e):
    if s >= e:
        return s
    mid = (s + e) // 2

    if arr[mid] <= v:
        return over_bound(arr, v, mid + 1, e)
    else:
        return over_bound(arr, v, s, mid)


# 배열에서 v를 초과하는 위치에서 시작하여, v를 초과하는 값을 합한 값을 반환
def get_over_sum(arr, v):
    bound_idx = over_bound(arr, v, 0, len(arr))

    over_sum = 0
    for i in range(bound_idx, len(arr)):
        over_v = arr[i] - v
        over_sum += over_v

    return over_sum


print(total_under_bound(trees, m) - 1)
