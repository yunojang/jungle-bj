import sys

input = sys.stdin.readlines
heights = list(map(lambda x: int(x.strip()), input()))


# arr 뒤로, idx부터 조합해 합이 100인 조합 배열을 반환하는 함수
def search_sum_100(idx, arr, total=0):
    if total == 100 and len(arr) == 7:
        return arr

    if total > 100 or len(arr) >= 7:
        return False

    for i in range(idx, len(heights)):
        cur = heights[i]
        res = search_sum_100(i + 1, arr + [cur], total + cur)
        if res:
            return res


for n in sorted(search_sum_100(0, [])):
    print(n)

# 개선
## 10명중 7명 조합 -> 전체 합을 구한 뒤 10명중 2명 조합
## 로직 복잡 및 반환 타입이 일관적이지 않음 -> target 의도를 드러내고 반환타입을 일관화
