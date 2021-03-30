from sys import stdin
from itertools import permutations

in1, in2 = map(int, stdin.readline().strip().split())
in3 = list(map(int, stdin.readline().strip().split()))
in3 = sorted(in3)
if in2 == 1:
    for i in in3:
        print(i)
else:
    ans = list(permutations(in3, in2))
    for i in ans:
        print(*i)