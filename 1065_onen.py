n = int(input())

# n 보다 크거나 같은 한수의 개수
def is_hansu(n):
    s = str(n)
    diff = None
    for i in range(1, len(s)):
        cd = int(s[i]) - int(s[i-1])
        if diff is not None and diff != cd:
            return False
        else:
            diff = cd
    return True
        

count = 0
for i in range(1, n+1):
    if is_hansu(i):
        count += 1
print(count)
