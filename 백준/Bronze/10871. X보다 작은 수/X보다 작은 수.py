n, x = tuple(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))

for n in nums:
    if n < x:
        print(n, end=" ")
