# nCk 이항계수
# 1초에 n은 4백만 이하

from sys import stdin
def cal1(n):
    cal = 1
    for i in range(2, n+1):
        cal = cal * i % 1000000007
    return cal

def cal2(n,k):
    if n==0:
        return 1
    temp = cal2(n//2, k)
    temp = temp * temp % 1000000007
    if n % 2 ==0:
        return temp
    else:
        temp = temp * k % 1000000007
        return temp

in1, in2 = map(int, stdin.readline().strip().split())
print(( cal1(in1) * cal2(1000000005, cal1(in2)) * cal2(1000000005, cal1(in1 - in2))) % 1000000007)