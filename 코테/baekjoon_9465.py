# dp
from sys import stdin
from collections import deque

in1 = int(stdin.readline().strip())
ans = []
for i in range(in1):
    in2 = int(stdin.readline().strip())
    in3 = list(map(int, stdin.readline().strip().split()))
    in4 = list(map(int, stdin.readline().strip().split()))
    an = deque()
    an.append([in3[0], 'up'])
    an.append([in4[0], 'up'])
    for i in range(1, in2):
        dp[0] = max([])


for i in ans:
    print(i)