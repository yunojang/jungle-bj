import sys
import math

inputs = sys.stdin.readlines()
t = int(inputs[0])
nums = list(map(int, inputs[1:]))


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gold(n):
    for i in range(int(n / 2), 1, -1):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return (0, 0)


# def gold1(n):
#     pass

# n까지의 소수를 모두 구한다 (에라토스테네스) - O(N)
# - n크기의 1~n까지 담긴 배열을 만든다
# - n제곱근 까지의 소수를 구한다 (2부터)
# - 배열에서 소수 목록의 배수는 모두 제외한다.

# n의 절반값에서 가까운 소수를 찾는다. - O(N)
# 그 수의 n의 보수가 소수에 있는지 찾는다. - O(N)
# 없다면, 이전 소수로 이동


for num in nums:
    x, y = gold(num)
    print(f"{x} {y}")
