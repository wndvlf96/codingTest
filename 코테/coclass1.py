#20163891 컴퓨터공학과 박중필
#---레벨1
#회문인데 글자 하나 달라도됨
def rec(str1):
    list1 = []
    for i in str1:
        list1.append(i)
    print(list1)
    list2 = list1.reverse()
    tot = 0
    if list1 == list2:
        return True
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            tot = tot+1
    if tot < 2:
        return True
    return False
#---------------레벨2----------------------------
#<단어 나누기> "str"을 arr의 문자열들을 이용해 나누어 떨어트릴수 있는지 TF 반환
def splitWord(str1,arr1):
    for i in arr1:
        str1 = str1.replace(i,'')
    if str1=='':
        return True
    return False

#<문자열 디코딩>
def decodingStr(str1):
    str1 = str1 + '$'         #$는 끝나는 표시
    stk =[]
    ans = ""
    for i in str1:
        if ord('0') <= ord('i') <= ord('9'):    #숫자 만날 때
            stk.append(i)
        elif i == '[':                          #열리는 문구 만날 때
            stk.append(i)
        elif i == ']':                          #닫히는 문구 만날 때
            ans2 = ""
            x = stk.pop()
            while x != '[':
                ans2 = x +ans2
                x = stk.pop()
            #ans2를 거뀨로
            ans2 =  ans2 * int(stk.pop())
            for j in ans2:
                stk.append(j)
        elif i == '$':                          #끝나는 기호 만날 때
            for j in stk:
                ans = ans + j
            return ans
        else:                                   #알파벳 만날 때
            stk.append(i)

#---------------레벨2----------------------------
#---------------레벨3----------------------------
#<빗물잡기>
def rain(arr1):
    left = []
    right = []
    tot = 0
    for index in range(len(arr1)):
        #왼쪽부터 index시의 최대값
        left.append(max(arr1[0:index+1]))
        #오른쪽부터 index시의 최대값 얘는 거꾸로 되어있음
        right.append(max(arr1[len(arr1)-1-index:len(arr1)]))
    for index in range(len(arr1)):
        tot= tot + (min(left[index],right[len(arr1)-index-1])-arr1[index])
    return tot

#<정렬된 두 배열의 중앙값>
def midVal(arr1,arr2):
    arr3 = arr1+arr2
    arr3.sort()
    print(arr3)
    if len(arr3)%2 != 0:
        return arr3[(len(arr3)-1)//2]
    return (arr3[(len(arr3))//2-1]+arr3[(len(arr3))//2])/2

#---------------레벨2----------------------------
print('------------------20163891 컴퓨터공학과 박중필------------------')
print('------------------레벨2의 3번------------------')
print(splitWord("qweqwe123qwe",['qwe','123']))
print('------------------레벨2의 4번------------------')
print(decodingStr("ab2[cd3[ef]x2[yz]]"))
#---------------레벨3----------------------------
print('------------------레벨3의 1번------------------')
print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))
print('------------------레벨3의 2번------------------')
print(midVal([1,2,3,4,5,6,7,8,9,12],[4,17,18,600]))

rec("qwe")