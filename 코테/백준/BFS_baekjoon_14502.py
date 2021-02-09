# 인풋으로 받은 그래프를 변형(이 때 모든 경우에 대해 값 계산?)
from sys import stdin
from collections import deque
from itertools import combinations
import copy

def bfs(grp, num, tw):
    # 최초 2의 위치들 -> tw
    # 최초 0의 갯수 -> num
    global in1,in2
    deq = deque(tw)
    while deq:
        x,y = deq.popleft()
        #우
        if y < in2-1:
            if grp[x][y+1] == 0:
                grp[x][y+1] = 2
                deq.append([x,y+1])
                num = num- 1
        #좌
        if y > 0:
            if grp[x][y-1] == 0:
                grp[x][y-1] = 2
                deq.append([x,y-1])
                num = num - 1
        #하
        if x > 0:
            if grp[x-1][y] == 0:
                grp[x-1][y] = 2
                deq.append([x-1,y])
                num = num - 1
        #상
        if x < in1-1:
            if grp[x+1][y] == 0:
                grp[x+1][y] = 2
                deq.append([x+1,y])
                num = num - 1
    return num


global in1,in2
in1, in2 = map(int, stdin.readline().strip().split())
in3 = []
canbewall = []
twos = []
for i in range(in1):
    in3.append(list(map(int, stdin.readline().strip().split())))
    for j in range(in2):
        if in3[i][j] == 0:
            canbewall.append([i,j])
        elif in3[i][j] == 2:
            twos.append([i,j])
# canbewall 중 3개를 골라서 그 경우마다 실행
com = list(combinations(canbewall, 3))
ans = []
for i in range(len(com)):
    ex = copy.deepcopy(in3)
    for j in range(3):
        ex[com[i][j][0]][com[i][j][1]] = 1
    ans.append(bfs(ex, len(canbewall)-3, twos))
print(max(ans))