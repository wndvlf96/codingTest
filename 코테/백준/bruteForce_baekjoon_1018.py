# 체스판 비교하기
in1, in2 = map(int, input().split())
cal1 = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']]
cal2 = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']]
in3 = []
for i in range(in1):
    str1 = input()
    in4 = []
    for j in str1:
        in4.append(j)
    in3.append(in4)
temp = []
for i in range(in1-7):
    for j in range(in2-7):
        tm1 = 0
        tm2 = 0
        for x in range(8):
            for y in range(8):
                if cal1[x][y] == in3[i+x][j+y]:
                    continue
                else:
                    tm1 += 1
        for x in range(8):
            for y in range(8):
                if cal2[x][y] == in3[i+x][j+y]:
                    continue
                else:
                    tm2 += 1
        temp.append(tm1)
        temp.append(tm2)
print(min(temp))
print(temp)