import sys

input = sys.stdin.readline
n = int(input())


def dsum(n):
    return n + sum(map(int, str(n)))


res = 0
for i in range(1, n):
    if dsum(i) == n:
        res = i
        break


print(res)
