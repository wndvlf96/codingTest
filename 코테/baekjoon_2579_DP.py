# 인풋 1 : 계단 갯수
# 인풋 2 ~ : 각 계단의 점수
# 어웃풋 : 조건에 맞추었을 때 최대점수
# 조건 1 : 한번에 하나 혹은 두개 계단 오르기 가능
# 조건 2 : 연속된 3개 계단 밟기 불가능(이 때 시작점은 미포함)
# 조건 3 : 마지막은 반드시 밟기
# 점화식 : ans[i] = in2[i] + max([ans[i-2], ans[i-3]+in2[i-1]])

in1 = int(input())
in2 = [0]
ans = [0]
for i in range(in1):
    in2.append(int(input()))
    ans.append(0)
ans[1] = in2[1]
if in1 >=2:
    ans[2] = in2[1] + in2[2]
for i in range(3,in1+1):
    ans[i] = in2[i] + max([ans[i-2], ans[i-3] + in2[i-1]])

print(ans[in1])