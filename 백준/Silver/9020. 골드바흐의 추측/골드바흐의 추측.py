import sys
import math

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]


def is_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def get_gold(num):
    start = num // 2
    for diff in range(start):
        a = start - diff
        b = start + diff
        if is_prime(a) and is_prime(b):
            return (a, b)
    return (0, 0)


for num in nums:
    print(*get_gold(num))
