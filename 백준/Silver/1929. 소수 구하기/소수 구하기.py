s, e = list(map(int, input().split(" ")))


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# for i in range(s, e + 1):
#     if is_prime(i):
#         print(i)


def seiev(s, e):
    prime = [True] * (e + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(e**0.5) + 1):
        if prime[i]:
            for j in range(i * i, e + 1, i):
                prime[j] = False

    return [i for i, is_p in enumerate(prime) if is_p and i >= s]


for p in seiev(s, e):
    print(p)
