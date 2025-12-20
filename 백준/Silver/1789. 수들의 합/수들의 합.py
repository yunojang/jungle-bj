import sys
import math

input = sys.stdin.readline
s = int(input())
n = int((math.sqrt(1 + 8*s) - 1) // 2)
print(n)
