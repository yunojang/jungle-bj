def d(n: int) -> int:
    s = n
    while n:
        s += n % 10
        n //= 10
    return s


limit = 10000
made = [False] * (limit + 1)

for x in range(1, limit + 1):
    val = d(x)
    if val <= limit:
        made[val] = True

for x in range(1, limit + 1):
    if not made[x]:
        print(x)
