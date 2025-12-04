import sys

input = sys.stdin.readline
n = int(input())


def is_tnum(n):
    return "666" in str(n)


cur = 1
num = 666
while cur < n:
    num += 1
    if is_tnum(num):
        cur += 1

print(num)
