# 각 인덱스의 오큰수 출력하기
# 인풋1 : 리스트의 크기
# 인풋 2~: 요소들
from sys import stdin

in1 = int(stdin.readline())
in2 = list(map(int, stdin.readline().split()))
ans = [-1 for x in range(in1)]
stk_index = []
stk = []
stk_index.append(0)
stk.append(in2[0])
for i in range(1, in1):
    # stk에서 in2[i] 보다 작은 애가 있는지 확인하기
    index = []
    while stk != []:
        if in2[i] > stk[-1]:
            ans[stk_index[-1]] = in2[i]
            del stk[-1]
            del stk_index[-1]
        else:
            break
    stk.append(in2[i])
    stk_index.append(i)
print(*ans)