# 세자리 수의 두 수를 받아서 곱셈을 실행
# 이 때 두번째 수는 한 자리씩 곱해서 나중에 다 더하기
# 출력이 4개가 되게!!!

n1 = int(input())
n2 = int(input())

o1 = n1 * (n2%10)
o2 = n1 * (n2//10 % 10)
o3 = n1 * (n2//100)
print(o1)
print(o2)
print(o3)
print(o1+o2*10+o3*100)