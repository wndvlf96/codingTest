from sys import stdin
import heapq

in1 = int(stdin.readline().strip())
ans = []
hq = []
for i in range(in1):
    in2= int(stdin.readline().strip())
    if in2 == 0:
        if hq != []:
            ans.append(heapq.heappop(hq) * -1)
        else:
            ans.append(0)
    else:
        heapq.heappush(hq, -1 * in2)

for i in ans:
    print(i)