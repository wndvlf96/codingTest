# 정렬 후 빠르게 찾기 => 이진탐색 이용

from sys import stdin

def cal(src, dst, target):
    global in2
    while src <= dst:
        mid = (src + dst) // 2
        if in2[mid] == target:
            return 1
        elif in2[mid] < target:
            src = mid + 1
        else:
            dst = mid - 1
    return 0

global in2
in1 = int(stdin.readline().strip())
in2 = list(map(int, stdin.readline().strip().split()))
in3 = int(stdin.readline().strip())
in4 = list(map(int, stdin.readline().strip().split()))
in2 = in2[:in1]
in4 = in4[:in3]
in2 = sorted(in2)
ans = []
for i in in4:
    ans.append( cal(0, in1-1, i) )
print(*ans)