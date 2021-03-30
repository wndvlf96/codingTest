from sys import stdin

set1 = set([])
in1 = int(stdin.readline().strip())
ans = []
for i in range(in1):
    print(set1)
    in2 = stdin.readline().strip().split()
    if in2[0] == 'add':
        set1.add(int(in2[1]))
    elif in2[0] == 'remove':
        if int(in2[1]) in set1:
            set1.remove(int(in2[1]))
    elif in2[0] == 'check':
        if int(in2[1]) in set1:
            ans.append(1)
        else:
            ans.append(0)
    elif in2[0] == 'toggle':
        if int(in2[1]) in set1:
            set1.remove(int(in2[1]))
        else:
            set1.add(int(in2[1]))
    elif in2[0] == 'all':
        set1 = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        set1 = set([])
for i in ans:
    print(i)