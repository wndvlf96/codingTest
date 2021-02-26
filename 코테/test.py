from sys import stdin
import heapq

in1 = int(stdin.readline().strip())
in2 = list(map(int, stdin.readline().strip().split()))
set1 = list(set(in2))
heapq.heapify(set1)
idxs = {}
for i in range(len(in2)):
    if in2[i] not in idxs:
        idxs[in2[i]] = [i]
    else:
        idxs[in2[i]].append(i)
tmp = 0
while set1:
    x = heapq.heappop(set1)
    for i in idxs[x]:
        in2[i] = tmp
    tmp += 1
print(*in2)