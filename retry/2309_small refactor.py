# 개선
## 10명중 7명 조합 -> 전체 합을 구한 뒤 10명중 3명 조합
## 로직 복잡 및 반환 타입이 일관적이지 않음 -> target 의도를 드러내고 반환타입을 일관화

import sys

input = sys.stdin.readlines
heights = list(map(int, input()))
n = len(heights)
target = sum(heights) - 100
remove_cnt = len(heights) - 7


def dfs(idx, picked, total=0):
    if len(picked) == remove_cnt and total == target:
        return picked
    if idx >= n:
        return False
    if total > target:
        return False
    res = dfs(idx + 1, picked + [idx], total + heights[idx])
    if res:
        return res
    return dfs(idx + 1, picked, total)


removed = dfs(0, [])
removed_set = set(removed)
for h in sorted(heights[i] for i in range(n) if i not in removed_set):
    print(h)
