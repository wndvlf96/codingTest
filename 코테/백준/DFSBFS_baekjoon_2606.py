from sys import stdin
from collections import deque

ans = 0
in3 = {}
in1 = int(stdin.readline().strip())
in2 = int(stdin.readline().strip())

for i in range(in2):
    in4, in5 = map(int, stdin.readline().strip().split())
    if in4 not in in3:
        in3[in4] = [in5]
    else:
        if in5 not in in3[in4]:
            in3[in4].append(in5)
    
    if in5 not in in3:
        in3[in5] = [in4]
    else:
        if in4 not in in3[in5]:
            in3[in5].append(in4)

deq = deque([1])
vit = set([1])

while deq:
    print(deq)
    now = deq.popleft()
    # now와 연결된 친구들중 vit에 없는 친구들만 deq과 vit에 넣으며 ans += 1
    for i in in3[now]:
        if i not in vit:
            deq.append(i)
            vit.add(i)
            ans += 1
print(ans)