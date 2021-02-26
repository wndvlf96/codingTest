from sys import stdin
from collections import deque

in1,in2 = map(int, stdin.readline().strip().split())
vit = [0]*(in1+1)
in3 = {}
for i in range(in2):
    a,b = map(int, stdin.readline().strip().split())
    if a not in in3:
        in3[a] = [b]
    else:
        if b not in in3[a]:
            in3[a].append(b)
    if b not in in3:
        in3[b] = [a]

    else:
        if a not in in3[b]:
            in3[b].append(a)

ans = 0
#1부터 vit[1] = 1로 하며 시작
for i in range(1,in1+1):
    if vit[i] == 0:
        ans += 1
        vit[i] = 1
        # bfs시작
        deq = deque([i])
        while deq:
            x = deq.popleft()
            if x in in3:
                for j in in3[x]:
                    if vit[j] == 0:
                        deq.append(j)
                        vit[j] = 1
print(ans)