from collections import deque

def calL(dst):
    global lh
    teml = lh
    dist = 0
    if teml == 1 or teml == 4 or teml == 7 or teml == 10:
        dist += 1
        teml += 1
    dist = (abs(teml - dst)//3)+dist
    return dist

def calR(dst):
    global rh
    temr = rh
    dist = 0
    if temr == 3 or temr == 6 or temr == 9 or temr == 12:
        dist += 1
        temr -= 1
    dist = (abs(temr - dst)//3)+dist
    return dist

def close(dst, hand):
    global lh, rh, answer
    if dst == 1 or dst == 4 or dst == 7:
        lh = dst
        answer = answer + "L"
    elif dst == 3 or dst == 6 or dst == 9:
        rh = dst
        answer = answer + "R"
    else:
        # 2, 5, 8, 0 누를 때
        if dst==0:
            dst = 11
        l = calL(dst)
        r = calR(dst)
        if l > r:
            rh = dst
            answer= answer + "R"
        elif r > l:
            lh = dst
            answer = answer + "L"
        else:
            if hand == "right":
                rh = dst
                answer = answer + "R"
            else:
                lh = dst
                answer = answer + "L"

def solution(numbers, hand):
    global lh, rh, answer
    deq = deque(numbers)
    answer = ''
    lh = 10                     # 별
    rh = 12                     # 샵
    while deq:
        close(deq.popleft(),hand)
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")