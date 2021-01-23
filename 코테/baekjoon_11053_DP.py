# 가장 긴 증가하는 부분 수열
# 첫 인풋은 1이상의 1000이하의 자연수

in1 = int(input())
in2 = list(map(int, input().split()))
ans = [1] * in1
for i in range(in1):
    for j in range(i):
        if in2[i] > in2[j]:
            ans[i] = max([ans[i], ans[j]+1])
print(max(ans))