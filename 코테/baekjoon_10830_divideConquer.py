# 크기가 in1 * in1 인 행렬을 in2승 만큼 했을 때 각 요소들의 값을 1000으로 나눈 나머지
# 시간제한 1초

from sys import stdin

def cal(b):
    global in1, in3
    if b == 0:
        temp1 = []
        for i in range(in1):
            temp2 = []
            for j in range(in1):
                if i == j:
                    temp2.append(1)
                else:
                    temp2.append(0)
            temp1.append(temp2)
        return temp1
    temp1 = cal(b//2)
    temp1 = mul(temp1,temp1)
    '''
    for i in range(in1):
        for j in range(in1):
            temp1[i][j] = temp1[i][j] % 1000
    '''
    if b % 2 == 0:
        return temp1
    else:
        temp1 = mul(temp1, in3)
        '''
        for i in range(in1):
            for j in range(in1):
                temp1[i][j] = temp1[i][j] % 1000
        '''
        return temp1

def mul(mat1, mat2):
    global in1, in3
    temp = [[0 for x in range(in1)]for y in range(in1)]
    for i in range(in1):
        for j in range(in1):
            for k in range(in1):
                temp[i][j] = temp[i][j] + (mat1[i][k] * mat2[k][j])
            temp[i][j] = temp[i][j] % 1000
    return temp

global in1, in3
in1, in2 = map(int, stdin.readline().strip().split())
in3 = []
for i in range(in1):
    in3.append(list(map(int, stdin.readline().strip().split())))
    
ans = cal(in2)
for i in ans:
    print(*i)