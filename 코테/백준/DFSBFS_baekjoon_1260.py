# dfs와 bfs의 결과
from sys import stdin
from collections import deque

def dfs(s):
    if visit_arr_dfs[s-1] == 0:
        print(s, end = ' ')
        visit_arr_dfs[s-1] = 1
        # 현재 있는거 빼고 연결 되어있는것들 중 수들 찾기
        li1 = []
        for i in in4:
            if s in i:
                # 자기자신과 연결되어있는경우
                if i[0] == i[1]:
                    continue
                # 첫번째와 동일해서 가는 곳이 두번째 요소일 경우
                elif i[0] == s:
                    if visit_arr_dfs[i[1]-1] == 0:
                        li1.append(i[1])
                        #visit_arr_dfs[i[1]-1] = 1 여기서 조정하면 실제로 더 위로 들어가야할 경우에 위로 못 들어감
                # 두번째와 동일해서 가는 곳이 첫번째 요소일 경우
                else:
                    if visit_arr_dfs[i[0]-1] == 0:
                        li1.append(i[0])
                        #visit_arr_dfs[i[0]-1] = 1 여기서 조정하면 실제로 더 위로 들어가야할 경우에 위로 못 들어감
        # 소트하는 이유: 작은 수 부터 해야 가장 작은 수를 먼저 dfs할 수 있음
        li1 = sorted(li1)
        for i in li1:
            dfs(i)

def bfs(s):
    # 현재 있는거 빼고 연결 되어있는것들 중 작은 수 부터  리스트뒤에 어펜드하기
    # 팝은 앞부터
    que = deque([s])
    while que:
        x = que.popleft()
        print(x, end=' ')
        li1=[]
        for i in in4:
            if x in i:
                # 자기자신과 연결되어있는경우
                if i[0] == i[1]:
                    continue
                # 첫번째와 동일해서 가는 곳이 두번째 요소일 경우
                elif i[0] == x:
                    if visit_arr_bfs[i[1]-1] == 0:
                        li1.append(i[1])
                        #visit_arr_dfs[i[1]-1] = 1 여기서 조정하면 실제로 더 위로 들어가야할 경우에 위로 못 들어감
                # 두번째와 동일해서 가는 곳이 첫번째 요소일 경우
                else:
                    if visit_arr_bfs[i[0]-1] == 0:
                        li1.append(i[0])
                        #visit_arr_dfs[i[0]-1] = 1 여기서 조정하면 실제로 더 위로 들어가야할 경우에 위로 못 들어감
        # 소트하는 이유: 작은 수 부터 어펜드해야지 가장 작은 수가 앞으로 오게댐
        li1 = sorted(li1)
        for i in li1:
            if visit_arr_bfs[i-1] == 0:
                que.append(i)
                visit_arr_bfs[i-1] = 1
    


in1, in2, in3 = map(int, stdin.readline().strip().split())
in4 = []
for i in range(in2):
    a, b = map(int, stdin.readline().strip().split())
    in4.append([a,b])

visit_arr_bfs= [0 for x in range(in1)]
visit_arr_bfs[in3-1] = [1]
visit_arr_dfs= [0 for x in range(in1)]
que_bfs = [in3]

dfs(in3)
print()
bfs(in3)