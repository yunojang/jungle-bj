n, k = list(map(int, input().split()))
goal = n - k
nums = str(input())

mono_dec_stack = []

for i in range(n):
    num = int(nums[i])
    while (
        mono_dec_stack
        and mono_dec_stack[-1] < num
        and len(mono_dec_stack) + (n - i) > goal
    ):
        mono_dec_stack.pop()
    mono_dec_stack.append(num)

print("".join(map(str, mono_dec_stack[:goal])))
