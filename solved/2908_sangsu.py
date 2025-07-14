ra, rb = tuple(map(reversed, input().split(" ")))

a = ""
b = ""
for da, db in zip(ra,rb):
    a += da
    b += db 

if int(a) > int(b):
    print(a)
else:
    print(b)