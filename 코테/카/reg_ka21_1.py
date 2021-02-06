import re

def solution(new_id):
    answer = ''
    # 대문자 -> 소문자
    new_id = new_id.lower()
    # 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    new_id = re.sub('[^a-z0-9-_.]','',new_id)
    # . 2개 이상이면 하나의 마침표로 치환
    new_id = re.sub('\.\.+','.',new_id)
    # .이 마지막이나 끝에 있다면 제거하기(하지만 이 .이 2개 이상일 경우는 0임)
    if new_id[0] == '.':
        new_id = new_id[1:len(new_id)]
    if len(new_id) >0:
        if new_id[len(new_id) - 1] == '.':
            new_id = new_id[0:len(new_id) - 1]
    # 빈 문자열이라면 a대입하기
    if len(new_id) == 0:
        new_id = 'a'
    # 16자 이상이면 첫 15개 문자 제외 제거 후, 이 때 마지막 문자(15번째문자)가 .이면 제거
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[len(new_id) - 1] == '.':
        new_id = new_id[0:len(new_id) - 1]
    #2자 이하라면 마지막 문자 길이가 3이 될때 까지 반복
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id) - 1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))