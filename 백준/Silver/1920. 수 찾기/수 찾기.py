import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split(" ")))
num_list.sort()

m = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split(" ")))


# arr의 s~e중 v가 있다면 1을 반환 없으면 0을 반환함
def binary_search(arr, v, s, e):
    if s >= e:
        return 0
    mid = (s + e) // 2

    if arr[mid] == v:
        return 1
    elif arr[mid] < v:
        return binary_search(arr, v, mid + 1, e)
    else:
        return binary_search(arr, v, s, mid)


for target in target_list:
    print(binary_search(num_list, target, 0, n))
