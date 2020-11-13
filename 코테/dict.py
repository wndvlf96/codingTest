def solution(participant, completion):
    answer = ''
    #참여자 명단에 있지만 완주자 명단에 없는 경우
    #참여자 명단에도 있고 완주자 명단에도 있지만 명수의 차이가 나는 경우
    cd = {}
    for c in completion:
        if c in cd:
            #num 증가시키기
            num = cd[c]
            num = num+1
            cd.update({c:num})
        else:
            cd.update({c:1})
            
    #여기서 pd하나씩 빼기
    for p in participant:
        if p in cd:
            #num 감소시키기
            num = cd[p]
            num = num-1
            if num == -1:
                answer = p
                return answer
            cd.update({p:num})
        else:
            answer = p
            return answer
    
    return answer


participant = ['josipa', 'filipa','marina', 'nikola','qwe']
completion = ['josipa', 'filipa','marina', 'nikola']
print(solution(participant, completion))