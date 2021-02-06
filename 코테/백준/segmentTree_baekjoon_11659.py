# 세그먼트 트리? prefix도 가능? (배열의 변화가 없음)를 이용하여 빠른 요소 접근하기

from sys import stdin



global in3
in1, in2 = map(int, stdin.readline().strip().split())               # in1 은 세그먼트 트리의 요소 갯수, in2는 테스트 갯수
in3 = list(map(int, stdin.readline().strip().split()))              # 이걸로 세트먼트 트리 만들어보자 (0번쨰는 비우고 1번째부터 2의k승까지 (in1 < 2의 k승))
sum = [0]
for i in range(1, in1+1):
    sum.append(sum[i-1] + in3[i-1])
ans = []
in4 = []                                                            # 각 테스트에서 사용할 요소 접근
for i in range(in2):
    a,b = map(int, stdin.readline().strip().split())
    in4.append([a, b])
    ans.append(sum[b] - sum[a-1])
for i in ans:
    print(i)