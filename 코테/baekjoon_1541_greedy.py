# 괄호가 없는 +,- 가 있는 식에서 값이 최소가 되게 식을 만들고 그 값을 출력
# 인풋 : 식, 아웃풋 : 결과

eq = input()
eq1 = eq.split('-')
ans = 0
for i in range(len(eq1)):
    if eq1[i] == "":
        continue
    # 문자열인 eq[i] 계산하기
    eq2 = eq1[i].split('+')
    an = 0
    for j in eq2:
        an += int(j)
    # i는 0이면 이 값은 양수 아니면 음수
    if i == 0:
        ans += an
    else:
        ans = ans - an
print(ans)