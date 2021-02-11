from sys import stdin
from collections import deque

in1, in2 = map(int, stdin.readline().strip().split())

timest = 0
posst = in1
while posst*2 < in2:
    posst *= 2
    timest += 1
deq = deque()
deq.append([posst,timest])
ans = 0
while deq:
    pos, time = deq.popleft()
    if pos == in2:
        ans = time
        break
    # *2 pos * 2 <= in2 라면 무조건 얘만 하지만 pos > in2 라면 하지말기
    # 이 때 계속 *2 해주기
    deq.append([pos*2, time+1])
    # +1 pos < in2 < pos*2 일 경우에만 실행
    deq.append([pos+1, time+1])
    # -1 pos > in2 라면 얘만 or pos < in2 < pos*2
    deq.append([pos-1, time+1])
    
print(ans)