# 단방향성의 길이 주어질 때
# 가장 루트가 될 수 있는 친구는?(가장 여러 노드를 탐색할 수 있는친구)
# DP + DFS -> 서로 재귀로 부르는 것을 막기 가능

from sys import stdin
import copy
from collections import deque
import sys


sys.setrecursionlimit(10001)
global in1,in2,in3, vit, lvit
in1, in2 = map(int, stdin.readline().strip().split())
in3 = {i:[] for i in range(1, in1+1)}
for i in range(in2):
    # a가 b를 신뢰한다
    # 즉 b를 해킹하면 a도 해킹가능!
    a, b = map(int, stdin.readline().strip().split())
    in3[b].append(a)

def dfs(num):
    global in1,in2,in3,vit
    for j in in3[num]:
        if lvit[num] == 0:
            if vit[j] == 0:
                vit[j] = 1
                dfs(j)
                for k in in3[j]:
                    if k not in in3[num]:
                        in3[num].append(k)
        
answer = []
mans = 0
lvit = [0 for i in range(in1+1)]
for i in range(1, in1+1):
    vit = [0 for j in range(in1+1)]
    dfs(i)
    lvit[i] = 1
    n = len(in3[i])
    if n > mans:
        mans = n
        answer = [i]
    elif n == mans:
        answer.append(i)
print(in3)
print(*answer)