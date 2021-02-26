# 1,2,3을 더해서 n을 만들 수 있는 경우의 수
# 1+1+1 = 3 
# 1 + 2 = 3
# 2 + 1 = 3
# 3     = 3
from sys import stdin
in1 = int(stdin.readline().strip())
an = [0] * 15
an[0] = 1
for i in range(12):
    an[i+1] = an[i+1] + an[i]
    an[i+2] = an[i] + an[i+2]
    an[i+3] = an[i] + an[i+3]


ans = []
for i in range(in1):
    in2 = int(stdin.readline().strip())
    ans.append(an[in2])
for i in ans:
    print(i)
