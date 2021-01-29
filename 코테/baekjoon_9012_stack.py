# 괄호가 여닫이 맞는지 TF 출력
from sys import stdin

in1 = int(stdin.readline())
ans = []
for i in range(in1):
    str1 = str(stdin.readline())
    stk = []
    if (len(str1)-1) % 2 ==0:
        for j in str1:
            # 스택 안 비었다면
            if stk != []:
                if j == ')' and stk[-1] == '(':
                    del stk[-1]
                else:
                    stk.append(j)
            # 스택 비어있다면
            else:
                stk.append(j)
        if stk == ['\n']:
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        ans.append("NO")
for i in ans:
    print(i)