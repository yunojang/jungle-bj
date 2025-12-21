import sys

input = sys.stdin.readline
s = int(input())

# s가 주어질때 가장 작은 수: 1 부터 1,2,3...
# 1~n 의 합 -> n(n+1) /2
# n(n+1) / 2 < s가 성립하는 가장 큰 n을 구해야한다. (n^2 + n) < s * 2

cnt = 1
while s != 0:
    if s >= cnt:
        s -= cnt
        cnt += 1
    else:
        break

print(cnt - 1)


# import math

# n = int((math.sqrt(1 + 8 * s) - 1) // 2)
