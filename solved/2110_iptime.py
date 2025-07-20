# 구하려는 거리를 이분 탐색으로 구한다 (나무자르는 높이를 구한 것 처럼)
import sys

n, c = list(map(int, sys.stdin.readline().split(" ")))
routers = list(map(int, sys.stdin.readlines()))

routers.sort()
l = routers[len(routers) - 1] - routers[0]
# L을 c-1등분으로 나눔 -> 최대거리
max_d = l // (c - 1)


# max는 경계값 주의
# arr에서 c개를 고를 때, 고른 값들 끼리의 최소 거리가 (min,max) 범위 내에서 최대가 되는 거리를 반환
def get_max_d(arr, c, min=1, max=max_d + 1):
    # 영역이 제로일땐, 그냥 그 위치가 삽입 위치임 (초과든 이상이든 다른값 무의미)
    if min >= max:
        return min
    mid = (min + max) // 2
    if is_possible_dist(arr, mid, c):
        return get_max_d(arr, c, mid + 1, max)
    else:
        return get_max_d(arr, c, min, mid)


# arr 요소들이 d 거리를 두고 c개 선택될 수 있는지 반환
def is_possible_dist(arr, d, c):
    # 0번 위치에 배치하고 시작
    s = 0
    c -= 1
    while c > 0:
        s = dist_lower_bound(arr, arr[s] + d, s, len(arr))
        # arr 범위를 넘어서는 곳에 넣는다면 실패
        if s >= len(arr):
            return False
        c -= 1
    return True


# arr에서 s~e 중, d값 이상이 처음 등장하는 위치
def dist_lower_bound(arr, d, s, e):
    if s >= e:
        return s
    mid = (s + e) // 2
    if d <= arr[mid]:
        return dist_lower_bound(arr, d, s, mid)
    else:
        return dist_lower_bound(arr, d, mid + 1, e)


print(get_max_d(routers, c) - 1)
