# 트리의 지름
from sys import stdin
from collections import deque
import copy

in1 = int(stdin.readline().strip())
in2 = {}
# 항상 노드의 개수-1 만큼의 간선이 생김(중복 간선이 없다면!
for i in range(in1-1):
    a,b,c, = map(int, stdin.readline().strip().split())
    if a not in in2:
        in2[a] = [[b,c]]
    else:
        in2[a].append([b, c])
    if b not in in2:
        in2[b] = [[a,c]]
    else:
        in2[b].append([a, c])

# DFS
stk1 = deque()
stk1.append([1, 0])
fin_weight = 0
fin_node = 1
vit1 = [1]
while stk1:
    cur_node, cur_weight = stk1.pop()
    if fin_weight < cur_weight:
        fin_weight = cur_weight
        fin_node = cur_node
    if cur_node in in2:
        for next_node, next_weight in in2[cur_node]:
            if next_node not in vit1:
                stk1.append([next_node, cur_weight + next_weight])
                vit1.append(next_node)

# DFS
stk1 = deque()
stk1.append([fin_node, 0])
fin_weight = 0
vit1 = [fin_node]
while stk1:
    cur_node, cur_weight = stk1.pop()
    if fin_weight < cur_weight:
        fin_weight = cur_weight
        fin_node = cur_node
    if cur_node in in2:
        for next_node, next_weight in in2[cur_node]:
            if next_node not in vit1:
                stk1.append([next_node, cur_weight + next_weight])
                vit1.append(next_node)
print(fin_weight)
'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

이때 45
'''