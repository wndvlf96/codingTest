# 인풋 1: 테스트 케이스의 갯수
# 인풋 2 ~ N-1 : 각 테스트 케이스
# 아웃풋 1 ~ N : 각 테스트 케이스의 결과
# 정삼각형 나선형으로 이어붙이기 각 결과값은 테스트 케이스로 들어온 번째의 정삼각형의 한 변의 길이
# 점화식 : f(n) = f(n-3) + f(n-2)

in1 = int(input())
in2 = []
for i in range(in1):
    in2.append(int(input()))
ans = [1 for x in range(max(in2))]
if max(in2) > 3:
    for i in range(3,max(in2)):
        ans[i] = ans[i-3] + ans[i-2]
for i in in2:
    print(ans[i-1])