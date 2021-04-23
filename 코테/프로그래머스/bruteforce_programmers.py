from collections import deque
def solution(numbers, target):
    answer = 0
    # numbers의 요소는 모두 음이 아닌 정수!
    deq = deque([])
    deq.append(numbers[0])
    deq.append(numbers[0] * -1)
    for i in range(1, len(numbers)):
        deq_temp = []
        while deq:
            now = deq.popleft()
            deq_temp.append(now + numbers[i])
            deq_temp.append(now - numbers[i])
        for j in deq_temp:
            deq.append(j)
    for i in deq:
        if i == target:
            answer += 1
    return answer