# input1: N명의 사람들, input2: 각 사람들이 걸리는 시간들을 한줄에 띄어쓰기로 받아오기
# output: N명의 사람들의 각각 걸린 시간의 합의 최소값

n = int(input())
data = list(map(int,input().split()))
data = data[0:n]

#데이터 오름차순 정리
data = sorted(data)
ans = 0

#i번째 데이터는 n-i만큼 반복되는 것을 이용
for i in range(len(data)):
    ans = ans + (data[i] * (n-i))

print(ans)