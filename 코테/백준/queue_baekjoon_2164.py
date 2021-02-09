from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
deq = deque()
for i in range(1, in1+1):
    deq.appendleft(i)
if in1 == 1:
    print(1)
else:
    while deq:
        x1 = deq.pop()
        if len(deq) == 1:
            print(deq.pop())
            break
        else:
            x2 = deq.pop()
            deq.appendleft(x2)