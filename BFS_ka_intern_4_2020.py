from collections import deque

def solution(board):
    answer = 999999999
    number = len(board)
    # 코너(500원) 최소, 직선(100원) 최소
    deq = deque([])
    # r,c,cost, 진행방향(0없음,1상,2하,3좌,4우)
    deq.append([0,0,0,0])
    vit = [[999999999 for r in range(number)] for c in range(number)]
    #print(vit)
    vit[0][0] = 0
    while deq:
        r,c,m,d = deq.popleft()
        #상
        if r != 0:
            if board[r-1][c] == 0:
                # 진행방향 보기
                if d == 3 or d== 4:
                    if vit[r-1][c] >= m+600:
                        vit[r-1][c] = m+600
                        deq.append([r-1,c,m+600,1])
                else:
                    if vit[r-1][c] >= m+100:
                        vit[r-1][c] = m+100
                        deq.append([r-1,c,m+100,1])
        #하
        # 이 때는 [number-1][number-1]인지도 확인할것
        if r != number-1:
            if board[r+1][c] == 0:
                # 진행방향 보기
                if r+1 == number - 1 and c == number-1:
                    if d==3 or d== 4:
                        if answer > m + 600:
                            answer = m + 600
                    else:
                        if answer > m + 100:
                            answer = m + 100
                elif d == 3 or d ==4:
                    if vit[r+1][c] >= m+600:
                        vit[r+1][c] = m+600
                        deq.append([r+1,c,m+600,2])
                else:
                    if vit[r+1][c] >= m+100:
                        vit[r+1][c] >= m+100
                        deq.append([r+1,c,m+100,2])
        #좌
        if c != 0:
            if board[r][c-1] == 0:
                # 진행방향 보기
                if d == 1 or d== 2:
                    if vit[r][c-1] >= m+600:
                        vit[r][c-1] >= m+600
                        deq.append([r,c-1,m+600,3])
                else:
                    if vit[r][c-1] >= m+100:
                        vit[r][c-1] = m+100
                        deq.append([r,c-1,m+100,3])
        #우
        if c != number-1:
            if board[r][c+1] == 0:
                # 진행방향 보기
                if c+1 == number - 1 and r == number-1:
                    if d==1 or d== 2:
                        if answer > m + 600:
                            answer = m + 600
                    else:
                        if answer > m + 100:
                            answer = m + 100
                elif d == 1 or d ==2:
                    if vit[r][c+1] >= m + 600:
                        vit[r][c+1] = m + 600
                        deq.append([r,c+1,m+600,4])
                else:
                    if vit[r][c+1] >= m+100:
                        vit[r][c+1] >= m + 100
                        deq.append([r,c+1,m+100,4])
    return answer