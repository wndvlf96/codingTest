# 인풋 1: 숫자 갯수
# 인풋 2~ : 0이면 pop 아니면 push
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

in1 = int(input())
ans = []
for i in range(in1):
    in2 = int(input())
    if in2 == 0:
        ans.pop()
    else:
        ans.append(in2)
tot = 0
for i in ans:
    tot += i
print(tot)