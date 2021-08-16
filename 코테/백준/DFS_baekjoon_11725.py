from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
in2 = {}
ans = [0 for _ in range(in1+1)]
for i in range(in1-1):
    a, b = map(int, stdin.readline().strip().split())
    if a not in in2:
        in2[a] = [b]
    else:
        in2[a].append(b)
    if b not in in2:
        in2[b] = [a]
    else:
        in2[b].append(a)

vit = set([1])
stk = deque([])
stk.append([1, 0])

while stk:
    cur_node, cur_head = stk.pop()
    for i in in2[cur_node]:
        if i not in vit:
            stk.append([i, cur_node])
            ans[i] = cur_node
            vit.add(i)

for i in range(2, len(ans)):
    print(ans[i])

'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''