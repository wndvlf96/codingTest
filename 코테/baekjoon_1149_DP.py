# 인풋 1 : 집의 갯수(N)
# 인풋 2 ~ 집의 갯수(N) + 1 : 각 RGB 컬러의 비용 3개를 띄어쓰기로 받기
# 아웃풋 : 모든 집을 칠하는 비용의 최소값
# 조건 0 : 모든 집은 RGB중 꼭 한색깔로만 칠해야함!!!
# 조건 1 : 1번 2번 색 다르게
# 조건 2 : N, N-1 색 달라야함
# 조건 3 : i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 그러니까 이웃한 집끼리 색 달라야함!!!
# 점화식 f(n,r) = min(f(n-1, g), f(n-1, b)) + n번쨰의 r값


in1 = int(input())
in2 = []
for i in range(in1):
    r, g, b = map(int, input().split())
    in2.append([r,g,b])

for i in range(1, in1):
    in2[i][0] = in2[i][0] + min([in2[i-1][1], in2[i-1][2]])
    in2[i][1] = in2[i][1] + min([in2[i-1][0], in2[i-1][2]])
    in2[i][2] = in2[i][2] + min([in2[i-1][0], in2[i-1][1]])

print(min(in2[in1-1]))