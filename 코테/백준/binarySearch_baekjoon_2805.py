from sys import stdin

def bs(s, e):
    global in2,in3
    while s <= e: 
        # 이분탐색
        mid = (s+e) // 2
        log = 0                 #벌목된 나무 총합
        for i in in3:
            if i >= mid:
                log += i - mid
            else:               # 정렬이 된 상태여서 아니라면 브레이크
                break        
        if log >= in2:
            s = mid + 1
        else:
            e = mid - 1
    return e


global in2, in3
in1, in2 = map(int, stdin.readline().strip().split())
in3 = list(map(int, stdin.readline().strip().split()))

# 웃긴게 이거 소트 안하는게 시간이 근소하게 빠르더라...
in3 = sorted(in3, reverse = True)

print(bs(0, in3[0]))