from collections import deque

def sel(mov,board):
    for i in range(len(board)):
        if board[i][mov-1] == 0:
            # 비어있다면
            continue
        else:
            # 보드에서 지워주기
            tmp = board[i][mov-1]
            board[i][mov-1] = 0
            return tmp

def solution(board, moves):
    answer = 0
    deq = deque()
    for i in moves:
        x = sel(i, board)
        if x == None:
            continue
        if deq:
            if x == deq[0]:
            # 넣을 것이 deq의 탑과 같다면 deq leftpop
                answer+=2
                deq.popleft()
            else:
                deq.appendleft(x)
        else:
            # 아니라면 deq에 넣기
            deq.appendleft(x)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))