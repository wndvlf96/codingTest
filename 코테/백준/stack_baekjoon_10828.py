# 스택 구현
# 인풋 1: 명령 수 
# 인풋 2 ~ : 각 명령들 ex) push 5, pop, size, empty, top

in1 = int(input())
ans = []
answer = []
for i in range(in1):
    inst = input()
    if inst.find("push") != -1:
        ans.append(int(inst.split(" ")[1]))
    elif inst.find("pop") != -1:
        if len(ans) >= 1:
            answer.append(ans.pop())
        else:
            answer.append(-1)
    elif inst.find("size") != -1:
        answer.append(len(ans))
    elif inst.find("empty") != -1:
        if len(ans) >= 1:
            answer.append(0)
        else:
            answer.append(1)
    elif inst.find("top") != -1:
        if len(ans) >= 1:
            answer.append(ans[-1])
        else:
            answer.append(-1)
for i in answer:
    print(i)