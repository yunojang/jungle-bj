import sys

inputs = list(map(int, sys.stdin.readlines()))
n = inputs[0]
nums = inputs[1:]


def sum_r(n):
    cnt = [0]

    def sum(t=0):
        if t == n:
            cnt[0] += 1
            return
        for i in range(1, 4):
            if t + i > n:
                continue
            sum(t + i)

    sum()
    return cnt[0]


for num in nums:
    print(sum_r(num))
