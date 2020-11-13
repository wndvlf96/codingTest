# 숫자 N, K를 입력받아서 N을 K로 나누어서 떨어지면 나누고 아니면 1을 빼는 형식으로 진행
def UntilOne1(n,k):
    ans = 0
    while n>1:
        if n%k==0:
            n = n //k
            ans = ans + 1
        else:
            n = n-1
            ans = ans + 1
    print(ans)

# 숫자 N > K인 경우에는 계속 1을 빼는 것의 연속 -> N-1만큼 ans에 더하기
def UntilOne2(n,k):
    ans = 0
    while n>=k:
        if n%k==0:
            n = n //k
            ans = ans + 1
        else:
            n = n-1
            ans = ans + 1
    ans = ans + n -1
    print(ans)

UntilOne1(34,150)
UntilOne2(34,150)