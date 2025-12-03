import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))
maps = []

for i in range(n):
    maps.append(tuple(map(int, input().split())))
