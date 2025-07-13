import sys
import math

inputs = sys.stdin.readlines()
t = int(inputs[0])
nums = list(map(int, inputs[1:]))

def is_prime(n):
    if n <2:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gold(n):
    for i in range(int(n/2), 1, -1):
        if is_prime(i) and is_prime(n-i): 
            return (i , n-i)
    return (0,0)


for num in nums:
    x,y = gold(num)
    print(f"{x} {y}")

