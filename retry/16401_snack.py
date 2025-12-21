import sys

input = sys.stdin.readline
m, n = tuple(map(int, input().split()))
snacks = list(map(int, input().split()))

print(snacks[n - m])
