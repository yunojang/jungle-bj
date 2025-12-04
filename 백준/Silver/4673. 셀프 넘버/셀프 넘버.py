# def d(n):
#     return n + sum(map(int, str(n)))


def is_selfn(n):
    for s in range(1, min(n, len(str(n)) * 9 + 1)):
        if s == sum(map(int, str(n - s))):
            return False
    return True


for i in range(1, 10001):
    if is_selfn(i):
        print(i)
