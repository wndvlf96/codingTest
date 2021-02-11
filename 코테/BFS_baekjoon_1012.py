from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
ans = []
for i in range(in1):
    a,b,c = map(int, stdin.readline().strip().split())
    in2 = []
    for j in range(c):
        x,y = map(int, stdin.readline().strip().split())
        in2.append([x, y])

    # 이제부터 1끼리 붙어있는 것들 모으기
    an = 0
    vit = [0 for j in range(len(in2))]
    for j in range(len(in2)):
        if vit[j] == 0:
            vit[j] = 1
            an += 1
            
            deq = deque([in2[j]])
            while deq:
                pos = deq.popleft()
                for k in range(len(in2)):
                    if vit[k] == 0:
                        if pos[0] == in2[k][0] and abs(pos[1] - in2[k][1])==1:
                            vit[k] = 1
                            deq.append(in2[k])
                        elif pos[1] == in2[k][1] and abs(pos[0] - in2[k][0]) == 1:
                            vit[k] = 1
                            deq.append(in2[k])
    ans.append(an)
for i in ans:
    print(i)