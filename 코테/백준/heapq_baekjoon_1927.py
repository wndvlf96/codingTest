from sys import stdin
import heapq

in1 = int(stdin.readline().strip())
hq = []
ans = []
for i in range(in1):
    in2 = int(stdin.readline().strip())
    if in2 == 0:
        if hq == []:
            ans.append(0)
        else:
            ans.append(heapq.heappop(hq))
    else:
        heapq.heappush(hq, in2)

for i in ans:
    print(i)