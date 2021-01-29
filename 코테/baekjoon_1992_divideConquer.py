# 쿼드트리


def cal(arr, n):
    global ans
    flag = True
    temp = arr[0][0]
    for x in range(n):
        for y in range(n):
            if temp != arr[x][y]:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        if temp == 1:
            ans += "1"
        else:
            ans += "0"
    else:
        # 왼쪽 위
        arr1 = [col[0 : n//2] for col in arr[0 : n//2]]
        # 오른쪽 위
        arr2 = [col[n//2 : n] for col in arr[0 : n//2]]
        # 왼쪽 아래
        arr3 = [col[0 : n//2] for col in arr[n//2 : n]]
        # 오른쪽 아래
        arr4 = [col[n//2 : n] for col in arr[n//2 : n]]
        ans += "("
        cal(arr1, n//2)
        cal(arr2, n//2)
        cal(arr3, n//2)
        cal(arr4, n//2)
        ans += ")"

# 인풋 받기
in1 = int(input())
in2 = []
for i in range(in1):
    str1 = input()
    li1 = []
    for j in str1:
        li1.append(int(j))
    in2.append(li1)
global ans
ans = ""

# 사각형으로 나누기
cal(in2, in1)

# 정답 출력하기
print(ans)

