input = input()

pair = {")": "(", "]": "["}
point = {")": 2, "]": 3}


def get_v(str):
    stack = []

    for c in str:
        if c in pair:
            s = 0
            # 숫자 모두 빼기
            while stack and isinstance(stack[-1], int):
                s += stack.pop()
            # 짝 맞나 확인
            if not stack or stack.pop() != pair[c]:
                return 0
            # 계산된 값 넣기
            stack.append(s * point[c] if s else point[c])
        else:
            stack.append(c)

    t = 0
    for item in stack:
        if not isinstance(item, int):
            return 0
        else:
            t += item
    return t


print(get_v(input))
