# 덩치 키, 몸무게 순위 나타내기

in1 = int(input())
in2 = []
ans= [1 for i in range(in1)]
for i in range(in1):
    in2.append(list(map(int,input().split())))
for i in range(in1):
    for j in range(in1):
        if i == j:
            continue
        if in2[i][0] <in2[j][0] and in2[i][1] < in2[j][1]:
            ans[i] += 1
strans = str(ans)
strans = strans.replace('[','')
strans = strans.replace(']','')
strans = strans.replace(',','')
print(strans)