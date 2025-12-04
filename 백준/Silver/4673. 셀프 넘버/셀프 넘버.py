def d(n):
    return n + sum(map(int, str(n)))


limit = 10000
made = [False] * (limit + 1)

for x in range(1, limit + 1):
    val = d(x)
    if val <= limit:
        made[val] = True

for x in range(1, limit + 1):
    if not made[x]:
        print(x)
