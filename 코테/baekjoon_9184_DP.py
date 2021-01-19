# 한 함수 w라는 재귀함수가 있다.
# 인풋1 ~ N : w의 매개변수 3개 각 줄마다 띄어쓰기로 받기 
# 인풋 N+1 : -1 -1 -1을 입력하는 것이 마지막 입력이라는 표시
# 아웃풋 1 ~ N : w의 값 ===> w(50, 50, 50) = 1048576

def cal2(a,b,c):
    #global ans
    global x
    #print("%d %d %d"%(a,b,c))
    
    if x[a][b][c] == -9:
        if (a <= 0 or b <= 0 or c <= 0):
            return 1
        elif (a > 20 or b > 20 or c > 20):
            val = cal2(20,20,20)
            return val
        elif (a<b and b<c):
            val1 = cal2(a,b,c-1)
            val2 = cal2(a,b-1,c-1)
            val3 = cal2(a,b-1,c)
            val = val1 + val2 - val3
            x[a][b][c] = val
            return val
        else:
            val1 = cal2(a-1, b, c)
            val2 = cal2(a-1, b-1, c)
            val3 = cal2(a-1, b, c-1)
            val4 = cal2(a-1, b-1, c-1)
            val = val1 + val2 + val3 - val4
            x[a][b][c] = val
            return val
    else:
        return x[a][b][c]



in1 = []
while True:
    a,b,c = map(int,input().split())
    if(a == -1 and b == -1 and c == -1):
        break
    in1.append([a,b,c])

#global ans
global x
x = [[[-9 for col in range(51)] for row in range(51)] for depth in range(51)]
#ans=[[[-9]*51]*51]*51

for i in in1:
    if i[0] < 0 or i[1] < 0 or i[2] < 0:
        print("w(%d, %d, %d) = %d" %(i[0], i[1], i[2], 1))
    else:
        print("w(%d, %d, %d) = %d" %(i[0], i[1], i[2], cal2(i[0],i[1],i[2])))