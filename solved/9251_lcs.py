import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

lcs = 0

t = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            t[i][j] = t[i - 1][j - 1] + 1
        else:
            t[i][j] = max(t[i][j - 1], t[i - 1][j])
        lcs = max(lcs, t[i][j])

print(lcs)
