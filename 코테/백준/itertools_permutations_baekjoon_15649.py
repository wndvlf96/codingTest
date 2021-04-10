from sys import stdin
from itertools import permutations

in1, in2 = map(int, stdin.readline().strip().split())
list1 = range(1, in1+1)
ans = list(permutations(list1, in2))
for i in ans:
    print(*i)