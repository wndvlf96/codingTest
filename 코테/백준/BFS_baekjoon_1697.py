from sys import stdin
from collections import deque


# 입력단
in1, in2 = map(int, stdin.readline().strip().split())
if in1 == in2 :
    print(0)
elif in1 > in2:
    print(in1-in2)
else:
    timest = 0
    posst = in1
    if in1 == 0:
        posst += 1
        timest += 1
    
    if posst == in2:
        print(timest)
    else:
        deq = deque()
        deq.append([posst,timest])
        vit = set([posst])
        ans = 0

        # BFS단
        while deq:
            pos, time = deq.popleft()
            
            c1 = pos*2
            c2 = pos+1
            c3 = pos -1
            if c1 == in2 or c2 == in2 or c3 == in2:
                ans = time+1
                break
            if pos < in2:
                if c1 not in vit:
                    deq.append([c1, time+1])
                    vit.add(c1)
            if pos < in2:
                if c2 not in vit:
                    deq.append([c2, time+1])
                    vit.add(c2)
            if pos >0:
                if c3 not in vit:
                    deq.append([c3, time+1])
                    vit.add(c3)
            
        print(ans)