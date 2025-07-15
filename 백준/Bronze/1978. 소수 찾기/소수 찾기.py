import math

n = input()
nums = list(map(int,input().split(" ")))

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

count = 0
for n in nums:
    if is_prime(n):
        count += 1

print(count)