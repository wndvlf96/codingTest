# 거슬러 줘야할 돈을 input으로 넣으면 output으로 거스름돈 동전(500원 100원 50원 10원)의 최소 갯수를 알려준다

def cal1(money):
    ans = 0
    ans += money // 500
    money = money % 500
    ans += money // 100
    money = money % 100
    ans += money // 50
    money = money % 50
    ans += money // 10
    return ans

print(cal1(5180))