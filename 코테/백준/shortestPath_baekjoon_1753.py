# 다익스트라로 한 구간에서 어느 구간까지의 최단거리 구하기

import heapq

in1, in2 = map(int, input().split())
in3 = int(input())
in4 = {i : [] for i in range(1, in1+1)}

for i in range(in2):
    a,b,c = map(int, input().split())
    in4[a].append([b,c])
INF = float('inf')
dist = [INF] * (in1 + 1)
dist[in3] = 0
heap = []
heapq.heappush(heap, (0, in3))
while heap:
    val, src = heapq.heappop(heap)
    for dst, cost in in4[src]:
        if dist[dst] > dist[src] + cost:
            dist[dst] = dist[src] + cost
            heapq.heappush(heap, (dist[dst], dst))

for i in range(1, in1+1):
    if dist[i] ==INF:
        print("INF")
    else:
        print(dist[i])