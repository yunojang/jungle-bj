paren = str(input())

pair = {")":"(", "]": "["}
scores = {")":2, "]": 3}

stack = []

def get_score(paren):
    for p in paren:
        if p in pair:
            # 괄호 내에 들어가 있는 점수 모두 빼며 누산
            sum = 0
            while stack and isinstance(stack[-1], int):
                sum += stack.pop()
            # 괄호 쌍 안맞으면 0점 종료
            if not stack or stack[-1] != pair[p]:
                return 0
            stack.pop()
            # 계산된 점수 넣기
            paren_score = scores[p]
            stack.append(sum * paren_score if sum else paren_score)
        else:
            stack.append(p)
    t = 0
    for remain in stack:
        if not isinstance(remain, int):
            return 0
        t += remain
    return t

print(get_score(paren))