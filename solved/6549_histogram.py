import sys

inputs = sys.stdin.readlines()


# 주어진 높이들로, 만들 수 있는 최대 넓이 반환
def get_max_rect(hs):
    max_h = 0
    up_stack = []
    for i in range(len(hs)):
        up_stack.append(i)
    return max_h


for input in inputs:
    if input == "0\n":
        break

    n, *nums = list(map(int, input.split()))
    print(get_max_rect(nums + [0]))
