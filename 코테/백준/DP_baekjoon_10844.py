# N자리수의 계단수의 갯수 구하기

in1 = int(input())
data= []
# 각 마지막 자리수의 갯수
data.append([0,1,1,1,1,1,1,1,1,1])
for i in range(in1):
    # 위에서 ans[i-1]의 해당 하는 각 수들의 일의 자리수가 0 혹은 9이면 1개, 아니면 2개의 경우가 생김
    data.append([data[i][1],data[i][0]+data[i][2],data[i][1]+data[i][3],data[i][2]+data[i][4],data[i][3]+data[i][5],data[i][4]+data[i][6],data[i][5]+data[i][7],data[i][6]+data[i][8],data[i][7]+data[i][9],data[i][8]])
    print(data[i])
ans = 0
for i in range(10):
    ans += data[in1-1][i]
print(ans % 1000000000)