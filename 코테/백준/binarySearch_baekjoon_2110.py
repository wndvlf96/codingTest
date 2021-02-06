# 와이파이를 mid마다 설치시 가장 인접한 와이파이의 최대거리

from sys import stdin

def cal():
    global in3

global in3
in1, in2 = map(int, stdin.readline().strip().split())
in3 = []
for i in range(in1):
    in3.append(int(stdin.readline().strip()))
in3 = sorted(in3)

