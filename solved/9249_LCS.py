import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

t = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
max_len = 0
end_pos = -1

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            t[i][j] = t[i - 1][j - 1] + 1
            if t[i][j] > max_len:
                max_len = t[i][j]
                end_pos = i
        else:
            t[i][j] = 0


print(max_len)
# 문자열 자르는법은 최대 공통문자열의 인덱스를 기반으로 앞쪽값만 구하면 된다.
print(s1[end_pos - max_len : end_pos])
