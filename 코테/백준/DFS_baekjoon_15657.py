from sys import stdin
from collections import deque
import copy

n1, n2 = map(int, stdin.readline().strip().split())
n3 = list(map(int, stdin.readline().strip().split()))
n3 = sorted(n3, key=lambda x:(x))
n3_re = list(reversed(n3))

if n2 == 1:
    for i in n3:
        print(i)
else:
    ans = []
    for i in n3:
        deq = deque([])
        deq.append([i, 1, [i]])
        while deq:
            d, lv, cur = deq.popleft()
            if lv+1 == n2:
                for j in n3:
                    if d <= j:
                        d_cur = copy.deepcopy(cur)
                        d_cur.append(j)
                        if lv+1 == n2:
                            ans.append(d_cur)
                        else:
                            deq.appendleft([j, lv+1, d_cur])
            elif lv+1 < n2:
                for j in n3_re:
                    if d <= j:
                        d_cur = copy.deepcopy(cur)
                        d_cur.append(j)
                        deq.appendleft([j, lv+1, d_cur])

    for i in ans:
        for j in i:
            print(j, end=' ')
        print()
'''
4 2
9 8 7 1
'''