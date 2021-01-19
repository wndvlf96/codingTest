# 인풋 1 : 포도주 갯수
# 인풋 2 ~ : 각 포도주의 양
# 어웃풋 : 조건에 맞추었을 때 최대양
# 조건 1 : 연속된 3개 포도주 마시기 불가능
# 점화식 : ans[i] = max([ ans[i-1]], ans[i-2] + in2[i], ans[i-3] + in2[i-1] + in2[i] ])
# n >= 3 : n == 0,1일 때는 고정, 2일때 조건2개, 3일때 조건 3개

in1 = int(input())
in2 = [0]
ans = [0]
for i in range(in1):
    in2.append(int(input()))
    ans.append(0)
ans[1] = in2[1]

if in1 >= 2:
    ans[2] = ans[1] + in2[2]
if in1 >= 3:
    for i in range(3, in1+1):
        ans[i] = max([ ans[i-1], ans[i-2]+in2[i], ans[i-3]+in2[i-1]+in2[i] ])

print(ans[in1])