import sys

n, s = list(map(int, sys.stdin.readline().split(" ")))
nums = list(map(int, sys.stdin.readline().split(" ")))

cnt = 0


def sum(acc=0, start=0):
    global cnt

    if acc == s and start != 0:  # 목표 s가 0인 경우 있어서, start 체크
        cnt += 1  # s완성 후, 더 조합하여 나올 수 있기에, return 안함

    for i in range(start, n):
        sum(acc + nums[i], i + 1)


sum()
print(cnt)
