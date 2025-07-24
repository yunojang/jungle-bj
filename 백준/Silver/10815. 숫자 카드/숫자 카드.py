n = int(input())
A = list(map(int, input().split()))
is_a = dict()
for num in A:
    is_a[num] = True
m = int(input())
B = list(map(int, input().split()))
rst = []
for num in B:
    if is_a.get(num):
        print(1, end=' ')
    else:
        print(0, end=' ')