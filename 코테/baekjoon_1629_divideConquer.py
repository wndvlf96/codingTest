# a ** b % c
# 시간 초과 해결하기! -> 0.5초
# 나머지의 반복 찾기는 불가능 -> 수가 커지면 나머지의 동일한거 나올 때까지만해도 0.5초 초과
# b의 제곱승을 일반적으로 하면 총 b번 연산 필요 
# 하지만 b를 2로 나누면서 하면 2의 x승 만큼 연산을 줄일 수 있음

def cal(b):
    print(b)
    global in1, in3
    if b == 0:
        return 1
    temp = cal(b//2)
    temp = (temp * temp) % in3
    if b % 2 == 0 :
        return temp
    else:
        return (temp*in1) % in3

from sys import stdin
global in1, in3
in1, in2, in3 = map(int, stdin.readline().strip().split())

print(cal(in2))
''' 나머지 반복되는 구간 찾기
temp = []
val = 1
dst = 0
src = 0
for i in range(in2):
    val = in1 * val
    val = val % in3
    if val in temp:
        src = temp.index(val)
        # 현재 i 와 idx의 차이 +1 만큼의 요소들이 반복되어 들어갈 예정이니까 끝!
        dst = i-1
        break
    else:
        temp.append(val)
    print(temp)
print(temp[src + ((in2 - 1 - src) % (dst - src + 1))])
'''

# 답 확인용
#print(in1 ** in2 % in3)