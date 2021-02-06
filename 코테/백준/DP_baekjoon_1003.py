# 각 피보나치 수열의 0출력 회수와 1출력 횟수 보여주기
# 인풋1 : 테스트 케이스 갯수 
# 인풋2 ~ N-1 : 테스트 케이스 띄어쓰기의 숫자 엔터로 각각 받기
# 아웃풋 1 ~ N : 각 테스트케이스의 결과들

in1 = int(input())
in2 = []

for i in range(in1):
    in2.append(int(input()))
if in1 == 0:
    pass
else:
    maxval = max(in2)
    ans = [0,0]
    for i in range(maxval+1):
        ans.append([0,0])
    ans[0] = [1,0]
    ans[1] = [0,1]


    for i in range(maxval+1):
        if ans[i] == [0,0]:
            a = ans[i-1][0] + ans[i-2][0]
            b = ans[i-1][1] + ans[i-2][1]
            ans[i] = [a,b]

    for i in in2:
        print("%d %d" %(ans[i][0],ans[i][1]))