import sys

input = sys.stdin.readline
n = int(input())


def dsum(n):
    s = n
    while n:
        s += n % 10
        n //= 10
    return s


res = 0
for i in range(1, n):
    if dsum(i) == n:
        res = i
        break


print(res)
