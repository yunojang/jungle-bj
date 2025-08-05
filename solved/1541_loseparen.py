import sys

exp = sys.stdin.readline().strip()

s1 = exp.split("-")

res = 0
for i in range(len(s1)):
    plus_exp = s1[i]
    plused = sum(map(int, plus_exp.split("+")))
    res += plused if i == 0 else -plused

print(res)
