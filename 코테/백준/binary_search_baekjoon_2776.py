from sys import stdin

def bs(n, arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == n:
            return 1
        elif arr[mid] > n:
            right = mid -1
        else:
            left = mid +1
    return 0

ans = []
in1 = int(stdin.readline().strip())
for i in range(in1):
    in2 = int(stdin.readline().strip())
    in3 = list(map(int, stdin.readline().strip().split()))
    in4 = int(stdin.readline().strip())
    in5 = list(map(int, stdin.readline().strip().split()))
    in3 = sorted(in3)
    for j in in5:
        ans.append(bs(j, in3))
for i in ans:
    print(i)
