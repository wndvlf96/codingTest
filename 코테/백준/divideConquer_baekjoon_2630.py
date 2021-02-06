# n * n 크기의 색종이 각 칸마다 1 혹은 0 들어가는데 
# 0이 으로 만들어진 큰 정사각형 수, 1로 만들어진 큰 정사각형 수 출력하기

global one
global zero
one = 0
zero = 0

def cal(arr, n):
    global one
    global zero
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
            one += 1
        else:
            zero += 1
    else:
        arr1 = [col[0:n//2] for col in arr[0:n//2]]
        arr2 = [col[n//2:n] for col in arr[0:n//2]]
        arr3 = [col[0:n//2] for col in arr[n//2:n]]
        arr4 = [col[n//2:n] for col in arr[n//2:n]]
        cal(arr1, n//2)
        cal(arr2, n//2)
        cal(arr3, n//2)
        cal(arr4, n//2)



in1 = int(input())
in2 = []
for i in range(in1):
    in2.append(list(map(int, input().split())))
# 계속 반 씩(n/2) 잘라보며 실행
cal(in2, in1)
print(zero)
print(one)