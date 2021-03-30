from sys import stdin
from itertools import combinations

in1, in2 = map(int, stdin.readline().strip().split())
in3 = []
for i in range(in1):
    in3.append(i+1)
in3 = sorted(in3)
if in2 == 1:
    for i in in3:
        print(i)
else:
    ans = list(combinations(in3, in2))
    for i in ans:
        print(*i)