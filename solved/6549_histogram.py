import sys

inputs = sys.stdin.readlines()


# 주어진 높이들로, 만들 수 있는 최대 넓이 반환
def get_max_rect(heights):
    pass


for input in inputs:
    if input == "0\n":
        break

    n, *nums = list(map(int, input.split()))
    print(get_max_rect(nums))
