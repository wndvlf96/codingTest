# 처음 입력으로 2수를 받고 각 수는 쓰일 수 있는 동전의 종류, 만들어야하는 값
# 다음 입력으로는 각 줄마다 동전의 가치

n, tot = map(int,input().split())
data = []
for i in range(n):
    data.append(int(input()))

#데이터 내림차순 정렬
data = sorted(data, reverse= True)

# 가장 큰 친구부터 tot줄여가며 ans 늘려가기
ans = 0
for i in data:
    ans = ans + (tot // i)
    tot = tot % i
print(ans)