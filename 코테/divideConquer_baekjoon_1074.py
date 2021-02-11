from sys import stdin
import math

def cal(count):
    global n, r, c, ans
    seq = (2 ** (n-count))

    if count == n:
        # 좌상
        if r < seq and c < seq:
            pass
        # 우상
        elif r < seq and c >= seq:
            ans+=1
        # 좌하
        elif r >= seq and c < seq:
            ans += 2
        # 우하
        elif r >= seq and c >= seq:
            ans += 3
        print(ans)
    else:
        # 좌상
        if r < seq and c < seq:
            cal(count+1)
        # 우상
        elif r < seq and c >= seq:
            ans += seq ** 2
            c = c - seq
            cal(count+1)
        # 좌하
        elif r >= seq and c < seq:
            ans += (seq ** 2) * 2
            r = r - seq
            cal(count+1)
        # 우하
        elif r >= seq and c >= seq:
            ans += (seq ** 2) * 3
            r = r - seq
            c = c - seq
            cal(count+1)
    # 4개 구간으로 나누어서 r과c가 포함되는 구간만 재귀적으로 실행
    

global n,r,c,ans
ans = 0
n, r, c = map(int, stdin.readline().strip().split())
cal(1)