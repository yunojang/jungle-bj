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
for i in range(max(1, n - 9 * len(str(n))), n):
    if dsum(i) == n:
        res = i
        break


print(res)
