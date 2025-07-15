import math
a,b,v = list(map(int, input().split(" ")))

u = a-b
print(math.ceil((v-a) / u) + 1)