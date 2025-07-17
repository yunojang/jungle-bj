import sys

n = int(sys.stdin.readline())

cnt = 0


def new_num(num, start=False):
    global cnt
    cnt += 1

    if num == n and not start:
        return

    left = num // 10
    right = num % 10
    sum = left + right
    sum_right = sum % 10

    return new_num(int(str(right) + str(sum_right)))


new_num(n, True)
print(cnt - 1)
