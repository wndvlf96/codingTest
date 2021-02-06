from collections import deque
import copy
import heapq

def toright(deq):
    ans = 0
    while deq:
        x = deq.popleft()
        if x in deq:
            ans += 1
        else:
            deq.appendleft(x)
            break
    return ans
    
def toleft(deq):
    ans = 0
    while deq:
        x = deq.pop()
        if x in deq:
            ans -= 1
        else:
            deq.append(x)
            break
    return ans

def solution1(gems):
    # 1. 왼쪽 먼저 가고 그 후 오른쪽 가기
    # 2. 1. 을 반대로
    # 1. 과 2.  비교하기
    # 중간에 있는거에 대해 확인 불가능
    deq1 = deque(gems)
    deq2 = deque(gems)
    a1 = toright(deq1) + 1
    a2 = len(gems) + toleft(deq1)
    b2 = len(gems) + toleft(deq2)
    b1 = toright(deq2) + 1
    print(a1)
    print(a2)
    print(b1)
    print(b2)
    if a2 - a1 >= b2 - b1:
        return [b1,b2]
    else:
        return [a1,a2]
'''
def check(li, gems):
    flag = True
    for i in gems:
        if i in li:
            continue
        else:
            flag = False
            break
    return flag
'''
def solution(gems):
    # 투 포인터
    ans = []
    num = len(gems)
    li = gems
    gems = list(set(gems))
    src = 0
    dst = 0
    fsrc = 0
    fdst = 0
    kindnum = {}
    kind = set()
    lastdst = 0
    length = float('inf')
    for src in range(num):
        flag = False
        # src는 0부터
        # 이 때 end를 조건 만족할때까지 최소한으로 늘리기
        for dst in range(lastdst, num):
            if li[dst] not in kind:
                kindnum[li[dst]] = 1
                kind.add(li[dst])
            else:
                kindnum[li[dst]] += 1
            # 종류를 다 포함했다면
            if len(kind) == len(gems):
                # 일단 답 저장
                if abs(dst - src) < length:
                    length = abs(dst - src)
                    fsrc = src
                    fdst = dst
                
                # flag 교체해서 다음 src로 넘어가기
                flag = True
                lastdst = dst
                break

        if not flag:
            #  더 src증가 시킬 필요도 없음
            break
        # 이제 src한칸 이동할 껀데 이 src제외하고 li[src]가 있다면?
        if li[src] in kind:
            if kindnum[li[src]] == 1:
                del kindnum[li[src]]
                kind.remove(li[src])
            else:
                # 더 있다면 1만 빼주기
                kindnum[li[src]] -= 1
        
        # 현재 dst제거하기 위 반복에서 다시 넣을것이기 때문
        if li[lastdst] in kind:
            if kindnum[li[lastdst]] == 1:
                del kindnum[li[lastdst]]
                kind.remove(li[lastdst])
            else:
                kindnum[li[lastdst]] -= 1
    return [fsrc+1, fdst+1]
    

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["1", "3", "3", "3", "3","3","1","2"]))
print(solution(["2", "1", "3", "3", "3","3","3","2"]))
print(solution(["1", "2", "3", "3", "3","3","3","2", "4", "3", "1","3","3","2","2","2","2","1"]))
print(solution(["1", "2", "3","2", "4", "3", "1","3","3","2","1"]))