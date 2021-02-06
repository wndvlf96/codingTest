# 토마토 익히기 문제 하루에 하나씩 인접한 안 익은 토마토를 익혀버림
from sys import stdin
from collections import deque

in1, in2 = map(int, stdin.readline().strip().split())
in3 = []
for i in range(in2):
    in3.append(list(map(int, stdin.readline().strip().split())))
# 사실상 in3가 visit테이블이 된다!
visitTB = in3

# 1찾기! 위치를 좌표로 두자
pos = deque()
for i in range(in2):
    for j in range(in1):
        if in3[i][j] == 1:
            pos.append((i, j, 0))

minDay = 0

# BFS시작하는데 level계산하며
while pos:
    x = pos.popleft()           # x == (행, 렬, 레벨)
    if x[2] > minDay:
        minDay = x[2]
    #위
    if x[0] < in2-1:
        if visitTB[x[0]+1][x[1]] == 0:
            visitTB[x[0]+1][x[1]] = 1
            pos.append((x[0]+1, x[1], x[2]+1))
    #아래
    if x[0] > 0:
        if visitTB[x[0]-1][x[1]] == 0:
            visitTB[x[0]-1][x[1]] = 1
            pos.append((x[0]-1, x[1], x[2]+1))
    #좌
    if x[1] > 0:
        if visitTB[x[0]][x[1]-1] == 0:
            visitTB[x[0]][x[1]-1] = 1
            pos.append((x[0], x[1]-1, x[2]+1))
    #우
    if x[1] < in1-1:
        if visitTB[x[0]][x[1]+1] == 0:
            visitTB[x[0]][x[1]+1] = 1
            pos.append((x[0], x[1]+1, x[2]+1))


# TB에 0이 있는지 확인하며 하기(못 익는 친구 확인)
for i in range(in2):
    for j in range(in1):
        if visitTB[i][j] == 0:
            minDay = -1

print(minDay)