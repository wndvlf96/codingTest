# 인풋1: n개의 회의 
# 인풋 2 ~ n : 각 회의의  시작시간, 끝나는 시간
# 아웃풋: 최대의 가능한 회의 갯수

in1 = int(input())
in2 = []
for i in range(in1):
    a,b = map(int,input().split())
    in2.append([a,b])
in2 = sorted(in2, key = lambda x:(x[1],x[0]))
ans = 0
end = 0
for i in range(0,in1):
    if end <= in2[i][0]:
        ans += 1
        # 현 끝점을 다음꺼의 끝점으로 교체
        end = in2[i][1]
print(ans)