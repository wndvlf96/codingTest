# 다익스트라로 두 정점간 최단거리인데 경유점이 2개(순서x) 있음

from sys import stdin
import heapq

def cal(src):
    global in1
    global in3
    INF = float('inf')
    dist = [INF]*(in1+1)
    hq = []
    heapq.heappush(hq, (0, src))
    dist[src] = 0

    while hq:
        distNow, verNow = heapq.heappop(hq)
        for dst, cost in in3[verNow]:
            if dist[dst] > dist[verNow] + cost:
                dist[dst] = dist[verNow] + cost
                heapq.heappush(hq, (dist[dst], dst))
    return dist

global in1
global in3
in1, in2 = map(int, stdin.readline().strip().split())           # 정점 개수, 간선갯수
if in2 == 0:
    in4, in5 = map(int,stdin.readline().strip().split())            # 경유점 2개
    print(-1)
else:
    in3 = {i: [] for i in range(1, in1+1)}                          # 간선 정보
    for i in range(in2):
        a,b,c = map(int,stdin.readline().strip().split())
        # 중복간선 체크(비었거나, 있다해도 도착점이 b가 아니거나, 도착점이 b이지만 그 코스타가 낮은값이라면 넣기(마지막 경우는 갱신하기))
        flag = True
        for j in in3[a]:
            if j[0] == b and j[1] <= c:
                flag = False
        if flag:
            in3[a].append([b,c])
            in3[b].append([a,c])
            in3[b].append([a,c])
    in4, in5 = map(int,stdin.readline().strip().split())            # 경유점 2개

    # 시작 -> 경유점1 -> 경유점2 -> 도착 ? 시작 -> 경유점2 -> 경유점1 -> 도착
    # 위처럼 총 다익스트라 3번
    distSrc = cal(1)
    dist1 = cal(in4)
    dist2 = cal(in5)
    INF = float('inf')
    if min([(distSrc[in4] + dist1[in5] + dist2[in1]), (distSrc[in5] + dist2[in4] + dist1[in1])]) == INF:
        print(-1)
    else:
        print(min([(distSrc[in4] + dist1[in5] + dist2[in1]), (distSrc[in5] + dist2[in4] + dist1[in1])]))