n = int(input())


def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return [i for i, is_p in enumerate(prime) if is_p]


primes = sieve(n)
cnt = 0

sp = 0
ep = 0
sum = 0

while True:
    if sum >= n:
        if sum == n:
            cnt += 1
        sum -= primes[sp]
        sp += 1
    elif ep == len(primes):
        break
    else:
        sum += primes[ep]
        ep += 1


print(cnt)
