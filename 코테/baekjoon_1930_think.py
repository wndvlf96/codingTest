# 정사면체 회전했을 때 같은 수 인지 판별하기

from sys import stdin

in1 = int(stdin.readline().strip())
in2 = []
ans = []
for i in range(in1):
    in2.append(stdin.readline().strip().split())
    cal1 = in2[i][0:4]
    cal2 = in2[i][4:8]
    flag = False
    p1 = cal1[1:4]
    #밑 면 맞추기
    if cal1[0] == cal2[0]:    
        p2 = cal2[1:4] * 2
        # 옆 면 맞추기
        for j in range(3):
            if p1 == p2[j:j+3]:
                flag = True
                break
    if cal1[0] == cal2[1] and flag == False:
        p2 = [cal2[0], cal2[3], cal2[2]] * 2
        for j in range(3):
            if p1 == p2[j:j+3]:
                flag = True
                break
    if cal1[0] == cal2[2]  and flag == False:
        p2 = [cal2[3], cal2[0], cal2[1]] * 2
        for j in range(3):
            if p1 == p2[j:j+3]:
                flag = True
                break
    if cal1[0] == cal2[3] and flag == False:
        p2 = [cal2[2], cal2[1], cal2[0]] * 2
        for j in range(3):
            if p1 == p2[j:j+3]:
                flag = True
                break

    if flag == True:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i)