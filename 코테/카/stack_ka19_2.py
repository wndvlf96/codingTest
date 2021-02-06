from collections import deque

def solution(s):
    answer = []
    deq = deque()
    s = s[1:len(s)-1]
    # s=="{2},{2,4},{2,4,5}" 이런 형식이 됨
    st = ""
    st2 = []
    print(s)
    for i in s:
        if i == '{':
            # 중괄호 시작
            pass
        elif i == '}':
            # 중괄호가 끝날 때
            st2.append(int(st))
            st = ""
            deq.append(st2)
            st2 = []
        elif i == ',':
            # 이 경우는 2가지로 나뉨 => 1. 중괄호를 나눌 때, 2. 중괄호 안에서 나눌 때
            # st가 비어있다면 1. 경우
            # st가 비어있지 않다면 2. 경우
            if st == "":
                pass
            else:
                st2.append(int(st))
                st = ""
        else:
            st += i
        print(deq)

    for i in range(1, len(deq)+1):
        for j in range(len(deq)):
            if i == len(deq[j]):
                # 이 deq[j]중 현재 answer에 없는 친구를 append() 하기 항상 이때는 i == 1
                if answer == []:
                    answer.append(deq[j][0])
                else:
                    ans = 0
                    for k in deq[j]:
                        if k in answer:
                            pass
                        else:
                            ans = k
                            break
                    answer.append(ans)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))