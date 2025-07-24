import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cards.sort()

def has_card(cards, target, s, e):
    if s>=e:
        return False
    mid = (s+e) // 2
    if cards[mid] == target:
        return True
    elif cards[mid] < target:
        return has_card(cards,target, mid+1, e) 
    else:
        return has_card(cards,target, s, mid) 


for num in nums:
    print(1 if has_card(cards, num, 0, len(cards)) else 0)