# a 집합, b 집합 교집합?
from sys import stdin

in1, in2 = map(int, stdin.readline().strip().split())
set1 = set([])
set2 = set([])
for i in range(in1):
    set1.add(stdin.readline().strip())
for j in range(in2):
    set2.add(stdin.readline().strip())
set3 = set1 & set2
print(len(set3))
ans = list(set3)
ans = sorted(ans)
# 사전순으로 나열하기
for i in ans:
    print(i)