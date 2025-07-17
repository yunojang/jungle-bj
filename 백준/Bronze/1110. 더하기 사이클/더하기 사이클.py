import sys

n = int(sys.stdin.readline())


def new_num(num):
    left = num // 10
    right = num % 10
    sum = left + right
    sum_right = sum % 10

    return int(str(right) + str(sum_right))


cnt = 1
num = new_num(n)

while num != n:
    num = new_num(num)
    cnt += 1

print(cnt)