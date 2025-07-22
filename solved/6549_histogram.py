import sys

inputs = sys.stdin.readlines()

def get_max_rect(hs):
    max_h = 0
    mono_inc= []
    
    for i in range(len(hs)):
        while mono_inc and hs[mono_inc[-1]] > hs[i]:
            poped_idx = mono_inc.pop()
            width = i if not mono_inc else i - mono_inc[-1] - 1
            max_h = max(max_h, width * hs[poped_idx])
        mono_inc.append(i)
    return max_h


for input in inputs:
    if input == "0\n":
        break

    n, *nums = list(map(int, input.split()))
    print(get_max_rect(nums + [0]))
