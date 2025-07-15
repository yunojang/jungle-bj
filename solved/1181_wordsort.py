import sys

n = int(sys.stdin.readline())

words = set()
for i in range(n):
    words.add(sys.stdin.readline()[0:-1])


words = list(words)
words.sort()
words.sort(key=len)

for w in words:
    print(w)
