n = int(input())


def hanoi(n, source=1, target=3, remain=2):
    if n == 1:
        print(source, target)
        return

    hanoi(n - 1, source, remain, target)
    print(source, target)
    hanoi(n - 1, remain, target, source)


print(2**n - 1)
if n <= 20:
    hanoi(n)
