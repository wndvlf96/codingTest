from collections import deque
from sys import stdin
in1 = int(stdin.readline().strip())
in2 = {}
for i1 in range(in1):
    in2_sp = list(map(int, stdin.readline().strip().split()))
    # 0번째는 이어지는 친구
    h = int(in2_sp[0])
    in2[h] = [[in2_sp[1], in2_sp[2]]]
    # -1나올 때까지 반복
    for i2 in range(3, len(in2_sp), 2):
        if int(in2_sp[i2]) == -1:
            break
        in2[h].append( [ in2_sp[i2], in2_sp[i2 + 1] ] )

# DFS
stk1 = deque()
stk1.append([1, 0])
fin_weight = 0
fin_node = 1
vit1 = set([1])
while stk1:
    cur_node, cur_weight = stk1.pop()
    if fin_weight < cur_weight:
        fin_weight = cur_weight
        fin_node = cur_node
    if cur_node in in2:
        for next_node, next_weight in in2[cur_node]:
            if next_node not in vit1:
                stk1.append([next_node, cur_weight + next_weight])
                vit1.add(next_node)

# DFS
stk1 = deque()
stk1.append([fin_node, 0])
fin_weight = 0
vit1 = set([fin_node])
while stk1:
    cur_node, cur_weight = stk1.pop()
    if fin_weight < cur_weight:
        fin_weight = cur_weight
        fin_node = cur_node
    if cur_node in in2:
        for next_node, next_weight in in2[cur_node]:
            if next_node not in vit1:
                stk1.append([next_node, cur_weight + next_weight])
                vit1.add(next_node)
print(fin_weight)