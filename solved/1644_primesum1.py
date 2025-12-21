import sys
import math

input = sys.stdin.readline
n = int(input())
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(i * i, n + 1, i):
        is_prime[j] = False

primes = [x for x in range(len(is_prime)) if is_prime[x]]

cnt = 0
l = 0
r = 0
s = 2

while l < len(primes):
    if s == n:
        cnt += 1
    if s < n:
        r += 1
        if r == len(primes):
            break
        s += primes[r]
    else:
        s -= primes[l]
        l += 1

print(cnt)
