# 출발점과 목적지의 후보가 있다.
# 한 사람이 최단거리로 출발지에서 목적지로 이동할 때
# 이 사람의 이동중 이용한 도로를 알 때
# 목적지의 후보 중 목적지에 해당하는 목적지는?

from sys import stdin
import heapq

def cal(src, index):
    global dictList, verNum
    INF = float('inf')
    dist = [INF] * (verNum[index]+1)
    dist[src] = 0
    hq = []
    heapq.heappush(hq, (0,src))
    while hq:
        dontuse, nowVer = heapq.heappop(hq)
        for nextVer, cost in dictList[index][nowVer]:
            if dist[nextVer] > dist[nowVer] + cost:
                dist[nextVer] = dist[nowVer] + cost
                heapq.heappush(hq, (dist[nextVer], nextVer))
    return dist

global dictList, verNum
in1 = int(stdin.readline().strip())                                     # 테스트 케이스 갯수
verNum = []
roadNum = []
dstNum = []
infos = []
dictList = []
dstCand = []

for k in range(in1):
    in2, in3, in4 = map(int, stdin.readline().strip().split())              # 교차로, 도로, 목적지 각각의 수
    verNum.append(in2)
    roadNum.append(in3)
    dstNum.append(in4)
    in5, in6, in7 = map(int, stdin.readline().strip().split())              # 출발지, 이 두 교차로 사이의 도로를 지나갔음
    infos.append([in5, in6, in7])
    in8 = {i:[] for i in range(1, in2+1)}                                   # 사전: 한 교차로에서 갈 수 있는 교차로 + 그 도로의 가중치
    for i in range(in3):
        a, b, c = map(int, stdin.readline().strip().split())
        # 중복 간선 체크
        flag = True
        for j in in8[a]:
            if j[0] == b and j[1] <= c:
                flag = False
        if flag:
            in8[a].append([b,c])
            in8[b].append([a,c])
    dictList.append(in8)
    in9 = []                                                                # 목적지 후보들
    for i in range(in4):
        in9.append(int(stdin.readline().strip()))
    dstCand.append(in9)

INF = float('inf')
ans = []
for i in range(in1):
    distSrc = cal(infos[i][0],i)
    dist1 = cal(infos[i][1],i)
    dist2 = cal(infos[i][2],i)
    cand = sorted(dstCand[i])
    ans1= []
    for j in cand:
        realVal = distSrc[j]
        pred1 = distSrc[infos[i][1]] + dist1[infos[i][2]] + dist2[j]
        pred2 = distSrc[infos[i][2]] + dist2[infos[i][1]] + dist1[j]
        if realVal != INF:
            if realVal == pred1:
                ans1.append(j)
            elif realVal == pred2:
                ans1.append(j)
    ans.append(ans1)
for i in ans:
    print(*i)