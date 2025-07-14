import sys
n = int(sys.stdin.readline())
write = sys.stdout.write


def hanoi(n, s=1, e=3 ):
    if (n==0): 
        return 0

    remain = 6 - s - e # 1+2+3 = 6
    hanoi(n-1, s, remain, )
    print(s, e)
    hanoi(n-1, remain, e, )

print(2**n -1)
if (n<=20):
    hanoi(n,1,3)