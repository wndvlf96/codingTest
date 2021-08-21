from sys import stdin
from collections import deque
import copy

in1, in2 = map(int, stdin.readline().strip().split())
ans = []
if in2 == 1:
    for i in range(1, in1+1):
        print(i)
else:
    for i in range(1, in1+1):
        deq = deque([[i, 1, [i]]])
        while deq:
            d, lv, cur = deq.popleft()
            ans_cand = []
            if lv+1 == in2:
                for j in range(d, in1+1):
                    d_cur = copy.deepcopy(cur)
                    d_cur.append(j)
                    if lv+1 == in2:
                        ans.append(d_cur)
                    else:
                        deq.appendleft([j, lv+1, d_cur])
            elif lv+1 < in2:
                for j in range(in1, d-1, -1):
                    d_cur = copy.deepcopy(cur)
                    d_cur.append(j)
                    if lv+1 == in2:
                        ans.append(d_cur)
                        print(d_cur)
                    else:
                        deq.appendleft([j, lv+1, d_cur])
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()

'''
3 3
'''