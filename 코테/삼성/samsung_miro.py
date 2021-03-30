from sys import stdin
from collections import deque

in1,in2 = map(int, stdin.readline().strip().split())
in3 = []
rpos = []
bpos = []
ox = -1
oy = -1
for i in range(in1):
    in3_str = stdin.readline().strip()
    if 'R' in in3_str:
        rpos.append(i)
        rpos.append(in3_str.find('R'))
    if 'B' in in3_str:
        bpos.append(i)
        bpos.append(in3_str.find('B'))
    if 'O' in in3_str:
        ox = i
        oy = in3_str.find('O')
    in3.append(in3_str)

rque = deque()
rque.append([rpos[0],rpos[1],0])
bque = deque()
bque.append([bpos[0],bpos[1],0])
flagfinal = True
flagwhile = False
while rque:
    if flagwhile:
        break
    rx, ry, rtime = rque.popleft()
    bx, by, btime = bque.popleft()
    if rtime >= 10:
        break
    # up 사실상 오른쪽으로
    # B의 위 경로에 #를 만나기전 O가 존재하지 않으며
    # R의 바로 위가 #이 아닐경우 다음큐에 넣어도 된다.
    flagup = True
    upby = by
    while in3[bx][upby] != '#':
        if in3[bx][upby] == 'O':
            flagup = False
            break
        upby += 1
    if (in3[rx][ry+1] != '#' or in3[bx][by+1] != '#') and flagup:
        # rpos가 위로가는중에 O를 만나면 rtime+1 반환하며 끝
        upry = ry
        while in3[rx][upry] !='#':
            if in3[rx][upry] == 'O':
                flagfinal = False
                flagwhile = True
                print(rtime+1)
                break
            upry+=1
        if rx == bx and upry == upby:
            if ry > by:
                upby -= 1
            else:
                upry -= 1
        rque.append([rx, upry-1, rtime+1])
        bque.append([bx, upby-1, btime+1])
    # down 사실상 왼쪽으로
    flagdown = True
    downby = by
    while in3[bx][downby] != '#':
        if in3[bx][downby] == 'O':
            flagdown = False
            break
        downby -= 1
    if (in3[rx][ry-1] != '#' or in3[bx][by-1] != '#') and flagdown:
        # rpos가 위로가는중에 O를 만나면 rtime+1 반환하며 끝
        downry = ry
        while in3[rx][downry] !='#':
            if in3[rx][downry] == 'O':
                flagfinal = False
                flagwhile = True
                print(rtime+1)
                break
            downry-=1
        if rx == bx and downry == downby:
            if ry > by:
                downry += 1
            else:
                downby += 1
        rque.append([rx, downry+1, rtime+1])
        bque.append([bx, downby+1, btime+1])
    # right 사실상 아래로 가기
    flagright = True
    rightbx = bx
    while in3[rightbx][by] != '#':
        if in3[rightbx][by] == 'O':
            flagright = False
            break
        rightbx += 1
    if (in3[rx+1][ry] != '#' or in3[bx+1][by] != '#') and flagright:
        # rpos가 위로가는중에 O를 만나면 rtime+1 반환하며 끝
        rightrx = rx
        while in3[rightrx][ry] !='#':
            if in3[rightrx][ry] == 'O':
                flagfinal = False
                flagwhile = True
                print(rtime+1)
                break
            rightrx+=1
        if rightrx == rightbx and ry == by:
            if rx > bx:
                rightbx -= 1
            else:
                rightrx -= 1
        rque.append([rightrx-1, ry, rtime+1])
        bque.append([rightbx-1, by, btime+1])
    # left 사실상 위로가기
    flagleft = True
    leftbx = bx
    while in3[leftbx][by] != '#':
        if in3[leftbx][by] == 'O':
            flagleft = False
            break
        leftbx -= 1
    if (in3[rx-1][ry] != '#' or in3[bx-1][by] != '#') and flagleft:
        # rpos가 위로가는중에 O를 만나면 rtime+1 반환하며 끝
        leftrx = rx
        while in3[leftrx][ry] !='#':
            if in3[leftrx][ry] == 'O':
                flagfinal = False
                flagwhile = True
                print(rtime+1)
                break
            leftrx-=1
        if leftrx == leftbx and ry == by:
            if rx > bx:
                leftrx += 1
            else:
                leftbx += 1
        rque.append([leftrx+1, ry, rtime+1])
        bque.append([leftbx+1, by, btime+1])
if flagfinal:
    print(-1)