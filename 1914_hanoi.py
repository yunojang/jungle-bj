n = int(input())

def hanoi(n, s=1, e=3, p=True):
    if (n==0): 
        return 0

    remain = 6 - s - e # 1+2+3 = 6
    hanoi(n-1, s, remain, p)
    if p:
        print(s, e)
    hanoi(n-1, remain, e, p)

print(2**n -1)
hanoi(n,1,3,n<=20)