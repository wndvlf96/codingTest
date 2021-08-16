from sys import stdin
from collections import deque

in1, in2 = map(int, stdin.readline().strip().split())
tot = [[0 for _ in range(in1+1)]]
ans = []
for i in range(in1):
    in3_1 = list(map(int, stdin.readline().strip().split() ))
    tot_1 = [0]
    r_tot = 0
    for j in range(len(in3_1)):
        tot_1.append(in3_1[j] + r_tot + tot[i][j+1])
        r_tot = r_tot + in3_1[j]
    
    tot.append(tot_1)

for i in range(in2):
    ans_1 = 0
    r1,c1,r2,c2 = (map(int, stdin.readline().strip().split() ))
    ans_1 = tot[r2][c2] - tot[r1-1][c2] - tot[r2][c1-1] + tot[r1-1][c1-1]
    ans.append(ans_1)

for i in ans:
    print(i)

'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''