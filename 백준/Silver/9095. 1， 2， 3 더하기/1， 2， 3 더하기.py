import sys
n = int(sys.stdin.readline())

def sum(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return sum(n-1) + sum(n-2) + sum(n-3)

for _ in range(n):
    print(sum(int(sys.stdin.readline())))