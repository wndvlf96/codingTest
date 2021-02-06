from collections import deque
import copy

def mps(deq):
    deqm = lm(deq)
    deqp = lp(deqm)
    deqs = ls(deqp)
    return abs(deqs[0])
def msp(deq):
    deqm = lm(deq)
    deqs = ls(deqm)
    deqp = lp(deqs)
    return abs(deqp[0])
def pms(deq):
    deqp = lp(deq)
    deqm = lm(deqp)
    deqs = ls(deqm)
    return abs(deqs[0])
def psm(deq):
    deqp = lp(deq)
    deqs = ls(deqp)
    deqm = lm(deqs)
    return abs(deqm[0])
def smp(deq):
    deqs = ls(deq)
    deqm = lm(deqs)
    deqp = lp(deqm)
    return abs(deqp[0])
def spm(deq):
    deqs = ls(deq)
    deqp = lp(deqs)
    deqm = lm(deqp)
    return abs(deqm[0])

def lm(deq):
    cpdeq = copy.deepcopy(deq)
    # 곱셈만 계산하기
    deqm = deque()
    while cpdeq:
        x = cpdeq.popleft()
        if x == '*':
            deqm.append(int(deqm.pop()) * int(cpdeq.popleft()))
        else:
            deqm.append(x)
    return deqm

def lp(deq):
    cpdeq = copy.deepcopy(deq)
    # 덧셈만 계산하기
    deqm = deque()
    while cpdeq:
        x = cpdeq.popleft()
        if x == '+':
            deqm.append(int(deqm.pop()) + int(cpdeq.popleft()))
        else:
            deqm.append(x)
    return deqm

def ls(deq):
    cpdeq = copy.deepcopy(deq)
    # 뺄셈만 계산하기
    deqm = deque()
    while cpdeq:
        x = cpdeq.popleft()
        if x == '-':
            deqm.append(int(deqm.pop()) - int(cpdeq.popleft()))
        else:
            deqm.append(x)
    return deqm

def solution(expression):
    deq = deque()
    nstr = ""
    for i in expression:
        if i == '+' or i == '-' or i=='*':
            deq.append(nstr)
            deq.append(i)
            nstr = ""
        else:
            nstr += i
    deq.append(nstr)
    ans = []
    ans.append(mps(deq))
    ans.append(msp(deq))
    ans.append(pms(deq))
    ans.append(psm(deq))
    ans.append(smp(deq))
    ans.append(spm(deq))
    answer = max(ans)
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("3*2"))