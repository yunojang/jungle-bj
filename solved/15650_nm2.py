import sys

# 1~N까지의 자연수 중 길이가 M인 오른차순 수열을 모두 구하라
input = sys.stdin.readline
n, m = tuple(map(int, input().split()))


def func(nums=[], depth=0):
    if depth == m:
        print(*nums)
        return

    for i in range((nums[-1] if nums else 0) + 1, n + 1):
        func([*nums, i], depth + 1)


func()
