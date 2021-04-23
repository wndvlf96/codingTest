import datetime

def solution(lines):
    answer = 0
    # lines로 시작시간~끝시간 표만들기
    endtime = []
    starttime = []
    for i in range(len(lines)):
        strl = lines[i].split(' ')
        # [0] 은 날짜, 1은 끝시각, 3은 처리시간
        ststr = strl[0] +'-'+ strl[1]
        t = float(strl[2][:-1])
        t = datetime.timedelta(seconds = t)
        et = datetime.datetime.fromisoformat(ststr)
        endtime.append(et)
        starttime.append(et-t+datetime.timedelta(seconds = 0.001))
    # 표 만들었으면 1초당 최대 처리량 구하기(sliding window?)
    tot = starttime + endtime
    # 시작시간들 뒤에 끝나는 시간들
    onesec = datetime.timedelta(seconds = 1)
    for i in tot:
        res = 0
        for j in range(len(lines)):
            # start타임이 1초내에 실행
            if i <= starttime[j] < i + onesec:
                res += 1
            # 위가 아니며 end타임이 1초내에 실행
            elif i <= endtime[j] <= i + onesec:
                res += 1
            # 위가 아니며 starttime이 작거나 같고 endtime인 1초더한것보다 크거나 같은 경우
            elif i >= starttime[j] and i + onesec <= endtime[j]:
                res += 1
        if answer < res:
            answer = res
                
    return answer