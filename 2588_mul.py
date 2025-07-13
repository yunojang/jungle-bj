import sys

lines = sys.stdin.readlines()
a = int(lines[0])
b = lines[1]

r1 = int(a * int(b[2]))
r2 = int(a * int(b[1]))
r3 = int(a * int(b[0]))
r4 = r1 + r2 * 10 + r3 * 100


print(r1)
print(r2)
print(r3)
print(r4)
