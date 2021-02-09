from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
in2 = []
deq = deque([])
ans = []
for i in range(in1):
    inst = str(stdin.readline().strip())
    if len(inst) > 5:    #무조건 push
        num = int(inst.split(' ')[1])
        deq.append(num)
    elif inst == 'pop':
        if len(deq) == 0:
            ans.append(-1)
        else:
            ans.append(deq.popleft())
    elif inst == 'size':
        ans.append(len(deq))
    elif inst == 'empty':
        if len(deq)==0:
            ans.append(1)
        else:
            ans.append(0)
    elif inst == 'front':
        if len(deq) == 0:
            ans.append(-1)
        else:
            ans.append(deq[0])
    elif inst == 'back':
        if len(deq) == 0:
            ans.append(-1)
        else:
            x = deq.pop()
            ans.append(x)
            deq.append(x)
for i in ans:
    print(i)