import sys


def new_num(num):
    left = num // 10
    right = num % 10
    sum = left + right
    sum_right = sum % 10

    return right * 10 + sum_right


n = int(sys.stdin.readline())

cnt = 1
num = new_num(n)

while num != n:
    num = new_num(num)
    cnt += 1

print(cnt)
