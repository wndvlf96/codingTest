from sys import stdin

in1 = int(stdin.readline().strip())
in2 = list(map(int, stdin.readline().strip().split()))
in3 = int(stdin.readline().strip())
in4 = list(map(int, stdin.readline().strip().split()))
ans = []

dictin2 = {}
for i in in2:
    if i not in dictin2:
        dictin2[i] = 1
    else:
        dictin2[i] += 1
print(dictin2)
for i in in4:
    if i not in dictin2:
        ans.append(0)
    else:
        ans.append(dictin2[i])

'''시간초과
for i in in4:
    an = 0
    for j in in2:
        if j == i:
            an += 1
    ans.append(an)
'''
print(*ans)