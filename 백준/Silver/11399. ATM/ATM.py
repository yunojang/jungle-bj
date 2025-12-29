import sys

input = sys.stdin.readline
n = int(input())
times = list(map(int, input().split()))
times.sort()

res = 0
delay = 0
for t in times:
    delay += t
    res += delay

print(res)
