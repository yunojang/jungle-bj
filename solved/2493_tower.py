# 모노토닉 스택 - 단조 감소 (낮은값 모두 뺌)
n = int(input())
hs = list(map(int, input().split(" ")))

res = [0] * len(hs)
stack = []
for i in range(len(hs) - 1, -1, -1):
    while stack and hs[stack[-1]] < hs[i]:
        res[stack.pop()] = i + 1
    stack.append(i)

print(*res)
