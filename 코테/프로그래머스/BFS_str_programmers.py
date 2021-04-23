from collections import deque
def solution(begin, target, words):
    answer = 0
    deq = deque([])
    vit = [0 for _ in range(len(words))]
    deq.append([begin, answer])
    flag = False
    # words중에 한글자만 달라야 변경가능
    # begin과 target은 다름!!!
    while deq:
        now_word, now_cost = deq.popleft()
        # now_word와 words중 한글자만 다른친구는?
        # 모든 단어의 길이는 같다!
        for i in range(len(words)):
            sub = 0
            for j in range(len(words[i])):
                if words[i][j] != now_word[j]:
                    sub += 1
                if sub >= 2:
                    break
            if sub < 2:
                # 만약 target과 같다면?
                if words[i] == target:
                    answer = now_cost + 1
                    flag = True
                    break
                # 다르면?
                if vit[i] == 0:
                    vit[i] = 1
                    deq.append([words[i], now_cost+1])
        if flag:
            break
    return answer