from collections import deque
import copy

def solution(prices):
    # 오큰수
    # 스택에 자기보다 큰 수나 같은 수를 보면 현재 스택안의 모든 ans[index]들 +1하고 append하기
    # 스텍의 top보다 작은 수 만나면 pop실행
    # 위가 아니라 -1을 하자
    
    ans = []
    deq = deque(prices)
    while deq:
        an = 0
        pr = deq.popleft()
        for i in deq:
            an += 1
            if i < pr:
                break
        ans.append(an)
    print(ans)
    return ans

solution([1, 2, 3, 2, 3])
solution([5, 10, 16, 7, 6, 3, 20, 17])