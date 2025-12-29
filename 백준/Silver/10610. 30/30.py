import sys

input = sys.stdin.readline
n = list(map(int, input().strip()))
n.sort(reverse=True)

if sum(n) % 3 == 0 and n[-1] == 0:
    print("".join(map(str, n)))
else:
    print(-1)
