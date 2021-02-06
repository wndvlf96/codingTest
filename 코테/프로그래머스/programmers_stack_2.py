from collections import deque
def solution(progresses, speeds):
    answer = []
    deq_prog = deque(progresses)
    deq_sp = deque(speeds)
    date = 0
    while deq_prog:
        an = 0
        while deq_prog[0] + (deq_sp[0]*date) < 100:
            date += 1
        prog = deq_prog.popleft()
        sp = deq_sp.popleft()
        an += 1
        while deq_prog:
            if deq_prog[0] + (deq_sp[0]*date) >= 100: 
                deq_prog.popleft()
                deq_sp.popleft()
                an+=1
            else:
                break
        answer.append(an)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))