from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
in2 = int(stdin.readline().strip())
in3 = []
for i in range(in2):
    # 이때 1,1 은 절대 안들어온다.(1행 1열)
    in3.append(list(map(int, stdin.readline().strip().split())))
in4 = int(stdin.readline().strip())
in5 = deque()
in6 = deque()
for i in range(in4):
    # 이 때 a는 무조건 증가하는 형식으로 주어진다.(a 초후의 방향 전환)
    # D = 오른쪽, L = 왼쪽
    a, b = map(str, stdin.readline().strip().split())
    in5.append(int(a))
    in6.append(b)
# 이 때 몇 초후 끝나는지 출력하기(벽 혹은 자기한테 부딪힐 경우 끝남)
time = 1
# 0: (우)열 하나 증가
# 1: (하)
# 2: (좌)
# 3: (상)
sdir = 0
shead = [1,1]
stail = []
sbody = deque([])

while 1:
    if sdir==0:
        # 오른쪽으로 이동하는 경우
        if shead[1]+1 == in1+1:
            # 벽인 경우
            print(time)
            break

        if [shead[0], shead[1]+1] in sbody or [shead[0], shead[1]+1] == stail:
            # 자기 몸과 부딪히는 경우
            print(time)
            break

        if [shead[0], shead[1]+1] in in3:
            # 이 곳에 사과가 있는 경우
            in3.remove([shead[0], shead[1]+1])  # 사과 삭제
            if stail == []:
                # 현재 길이가 1일때
                stail = shead
            else:
                sbody.append([shead[0], shead[1]])
        else:
            # 사과가 없는 경우
            if stail == []:
                # 현재 길이가 1일때
                pass
            elif sbody == []:
                # 현재 길이가 2일때
                stail = shead
            else:
                # body에 head추가 및 마지막 tail이 될 친구 pop
                sbody.append([shead[0], shead[1]])
                stail = sbody.popleft()
        shead = [shead[0], shead[1]+1]      # 머리 이동

        
    if sdir==1:
        # 아래쪽으로 이동하는 경우
        if shead[0]+1 == in1+1:
            # 벽인 경우
            print(time)
            break

        if [shead[0]+1, shead[1]] in sbody or [shead[0]+1, shead[1]] == stail:
            # 자기 몸과 부딪히는 경우 이 때 머리 먼저 움직이고 꼬리 나중에 움직여서
            print(time)
            break

        if [shead[0]+1, shead[1]] in in3:
            # 이 곳에 사과가 있는 경우
            in3.remove([shead[0]+1, shead[1]])  # 사과 삭제
            if stail == []:
                # 현재 길이가 1일때
                stail = shead
            else:
                sbody.append([shead[0], shead[1]])
        else:
            # 사과가 없는 경우
            if stail == []:
                # 현재 길이가 1일때
                pass
            elif sbody == []:
                # 현재 길이가 2일때
                stail = shead
            else:
                # body에 head추가 및 마지막 tail이 될 친구 pop
                sbody.append([shead[0], shead[1]])
                stail = sbody.popleft()
        shead = [shead[0]+1, shead[1]]      # 머리 이동


    if sdir==2:
        # 왼쪽으로 이동하는 경우
        if shead[1]-1 == 0:
            # 벽인 경우
            print(time)
            break

        if [shead[0], shead[1]-1] in sbody or [shead[0], shead[1]-1] == stail:
            # 자기 몸과 부딪히는 경우
            print(time)
            break

        if [shead[0], shead[1]-1] in in3:
            # 이 곳에 사과가 있는 경우
            in3.remove([shead[0], shead[1]-1])  # 사과 삭제
            if stail == []:
                # 현재 길이가 1일때
                stail = shead
            else:
                sbody.append([shead[0], shead[1]])
        else:
            # 사과가 없는 경우
            if stail == []:
                # 현재 길이가 1일때
                pass
            elif sbody == []:
                # 현재 길이가 2일때
                stail = shead
            else:
                # body에 head추가 및 마지막 tail이 될 친구 pop
                sbody.append([shead[0], shead[1]])
                stail = sbody.popleft()
        shead = [shead[0], shead[1]-1]      # 머리 이동


    if sdir==3:
        # 위쪽으로 이동하는 경우
        if shead[0]-1 == 0:
            # 벽인 경우
            print(time)
            break

        if [shead[0]-1, shead[1]] in sbody or [shead[0]-1, shead[1]] == stail:
            # 자기 몸과 부딪히는 경우
            print(time)
            break

        if [shead[0]-1, shead[1]] in in3:
            # 이 곳에 사과가 있는 경우
            in3.remove([shead[0]-1, shead[1]])  # 사과 삭제
            if stail == []:
                # 현재 길이가 1일때
                stail = shead
            else:
                sbody.append([shead[0], shead[1]])
        else:
            # 사과가 없는 경우
            if stail == []:
                # 현재 길이가 1일때
                pass
            elif sbody == []:
                # 현재 길이가 2일때
                stail = shead
            else:
                # body에 head추가 및 마지막 tail이 될 친구 pop
                sbody.append([shead[0], shead[1]])
                stail = sbody.popleft()
        shead = [shead[0]-1, shead[1]]      # 머리 이동

    # 방향전환 적용
    if len(in5) > 0:
        if in5[0] == time:
            in5.popleft()
            where = in6.popleft()
            if where == 'D':
                sdir += 1
                sdir = sdir % 4
            else:
                sdir -= 1
                if sdir == -1:
                    sdir = 3

    time += 1