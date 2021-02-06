# 가로폭이 있는 그래프인 한 히스토그램에서 가장 큰 직사각형의 넓이 구하기
# 세그먼트 트리를 알고나서 다시해보자

from sys import stdin
import sys
import heapq

sys.setrecursionlimit(1000000)

def calLeft(in2, index, height):
    ans = 0
    if index > 0:
        if in2[index - 1] >= height:
            ans += height
            ans += calLeft(in2, index - 1, height)
    return ans

def calRight(in2, index, height):
    ans = 0
    if index < len(in2)-1:
        if in2[index+1] >= height:
            ans += height
            ans += calRight(in2, index + 1 ,height)
    return ans

ans = []
while True:
    in1 = list(map(int, stdin.readline().strip().split()))
    if in1 == [0]:
        break
    in2 = in1[1:]
    #big = [in1[0]]
    bighq = []
    heapq.heappush(bighq, (in1[0] * -1))
    temp = in2
    in3 = sorted(in2)
    for i in in3:
        tmp = temp.index(i)
        #big.append(calLeft(in2, tmp, i)+ calRight(in2, tmp,i) + i)
        heapq.heappush(bighq, ((calLeft(in2, tmp, i)+ calRight(in2, tmp,i) + i)*-1))
        temp[tmp] = -1
    ans.append(heapq.heappop(bighq) * -1)

for i in ans:
    print(i)

'''
# 10만개 테스트 케이스
in5 = [99999]
big2 = []
for i in range(99998):
    in5.append(i)
in6 = in5[1:]
temp = in6
in7 = sorted(in6)
for i in in7:
    tmp = temp.index(i)
    big2.append(calLeft(in6, tmp, i) + calRight(in6, tmp, i)+i)
    temp[tmp] = -1
print(max(big2))
'''