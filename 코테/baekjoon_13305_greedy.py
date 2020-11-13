# 인풋1: 도시의 갯수, 
# 인풋2: 일자 형태의 도시들 사이의 거리들 띄어쓰기로 
# 인풋3: 각 도시마다의 1리터당 기름값
# 아웃풋: 마지막 도시까지의 최소 돈

in1 = int(input())
in2 = list(map(int, input().split()))
in3 = list(map(int, input().split()))
ans = 0

#도시가 바뀔때 마다 기름값이 적으면 그 기름값으로 변경하며 움직이기
val = in3[0]
for i in range(in1 - 1):
    if val > in3[i]:
        val = in3[i]
    ans = ans + val * in2[i]
print(ans)