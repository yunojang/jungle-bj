import sys

input = sys.stdin.readline
s = int(input())

# s가 주어질때 가장 작은 수: 1 부터 1,2,3...
cnt = 1
while s != 0:
    if s >= cnt:
        s -= cnt
        cnt += 1
    else:
        break

print(cnt - 1)
