import sys

n, b = tuple(map(int, sys.stdin.readline().split()))
matrix = list(map(lambda l: list(map(int,l.split())), sys.stdin.readlines()))

def mul_matrix(m1, m2):
    mul = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += ((m1[i][k] % 1000) * (m2[k][j] % 1000)) % 1000
            mul[i][j] = s % 1000
    return mul

def mul_exp(m, b):
    if b == 1:
        return [[v%1000 for v in row] for row in m]
    half = mul_exp(m, b//2)

    if b % 2 == 0:
        return mul_matrix(half, half)
    else:
        return mul_matrix(m, mul_matrix(half, half))
    
for row in mul_exp(matrix, b):
    print(" ".join(list(map(str,row))))