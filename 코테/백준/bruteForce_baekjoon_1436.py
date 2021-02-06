# 666이 이것이 들어가는 수 중 n번째로 작은 수는?

in1 = int(input())

ans = [666]
i = 1666
while True:
    if len(ans) == in1:
        break
    stri = str(i)
    if stri.find("666") != -1:
        ans.append(i)
    i += 1
print(ans[-1])