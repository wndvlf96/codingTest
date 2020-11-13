# N과 문자열(L,R,U,D들로 이루어진)것을 받음
# 한번에 LR/ UD를 replace할 수 없음!!! <- 알파벳이 움직일 수 없는 경우가 있기 때문에
def mov(n,str):
    x=1
    y=1
    for i in str:
        #i에 앞글자 부터 순서대로 들어옴
        if i == 'L':
            if y == 1:
                continue
            else:
                y = y-1
        if i == 'R':
            if y == n:
                continue
            else:
                y = y + 1
        if i == 'U':
            if x == 1:
                continue
            else:
                x = x-1
        if i == 'D':
            if x == n:
                continue
            else:
                x = x + 1
    print(x,y)

mov(6,'LRRUDDDDDDLULRUDLRUDRLDUR')