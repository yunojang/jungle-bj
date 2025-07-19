a, b, c = list(map(int, input().split()))


# a를 exp번 만큼 곱하는 함수
def fast_exp(a, exp):
    if exp == 1:
        return a

    half = fast_exp(a, exp // 2)
    if exp % 2 == 0:
        return (half % c) * (half % c)
    else:
        return (a % c) * (half % c) * (half % c)


print(fast_exp(a, b) % c)
