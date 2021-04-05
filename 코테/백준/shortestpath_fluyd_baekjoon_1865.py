from sys import stdin
in1 = int(stdin.readline().strip())
ans = []
for i in range(in1):
    n, m, w = map(int, stdin.readline().strip().split())
    mapping = [[10001 for j_1 in range(n)]for j_2 in range(n)]
    # 각 n에서의 경로(최소의 값만 넣을것이다)
    for j in range(m):
        s,e,t = map(int, stdin.readline().strip().split())
        if mapping[s-1][e-1] > t:
            mapping[s-1][e-1] = t
        if mapping[e-1][s-1] > t:
            mapping[e-1][s-1] = t
    w_info = []
    for j in range(w):
        s,e,t =  map(int, stdin.readline().strip().split())
        if mapping[s-1][e-1] > (t * -1):
            mapping[s-1][e-1] = (t * -1)
    # n은 지점의 개수, m은 도로, w는 웜홀 개수
    # m_info, w_info에는 시작 -> 도착 걸리는 or 줄어드는 시간 정보 저장
    # 루프찾기 이 때 0미만
    # 플로이드 와샬 vs 다익스트라
    # 다익스트라는 한 점에서 모든 점까지의 최단경로
    # 플로이드 와샬은 모든점에서 모든점까지의 최단경로
    list1 = [i for i in range(n)]
    list1 = sorted(list1, reverse = True)
    for j_1 in list1:
        # 거쳐감
        for j_2 in range(n):
            # 출발
            for j_3 in range(n):
                #도착
                if mapping[j_2][j_3] > mapping[j_2][j_1] + mapping[j_1][j_3] and mapping[j_2][j_1] != 10001 and mapping[j_1][j_3] != 10001:
                    mapping[j_2][j_3] = mapping[j_2][j_1] + mapping[j_1][j_3]

    flag = False
    for j in range(n):
        if mapping[j][j] < 0:
            flag = True
    if flag:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)