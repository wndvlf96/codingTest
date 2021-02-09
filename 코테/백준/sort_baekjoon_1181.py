from sys import stdin

in2 = []
in1 = int(stdin.readline().strip())
for i in range(in1):
    q = str(stdin.readline().strip())
    in2.append([q, len(q)])
in2 = sorted(in2, key = lambda x : (x[1],x[0]))
ans = []
for i in in2:
    if i[0] not in ans:
        ans.append(i[0])
        print(i[0])