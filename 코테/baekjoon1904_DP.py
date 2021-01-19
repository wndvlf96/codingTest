# 피보나치2
# 인풋 : n
# 아웃풋 : 결과물
import sys

in1 = int(input())
if in1 == 1:
    print(1)
elif in1 == 2:
    print(2)
else:
    ans = [0 for x in range(in1 + 1)]
    ans[1] = 1
    ans[2] = 2
    for i in range(in1+1):
        if i > 2:
            ans[i] = (ans[i-1] + ans[i-2]) % 15746
    print(ans[in1])