import sys

input = sys.stdin.readline

while (num := input().strip()) != "0":
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            print("no")
            break
    else:
        print("yes")
