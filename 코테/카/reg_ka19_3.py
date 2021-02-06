def solution(user_id, banned_id):
    import re
    from itertools import product
    my_list = []
    # banned_id로 가능한 user_id들 만들기
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*', '.')
        # .은 메타문자로 줄바꿈을 제외한 모든 문자가 가능, $는 문자열의 마지막을 나타냄
        tmp = [id for id in user_id if len(re.findall('^' + banned_id[i] + '$', id)) > 0]
        my_list.append(tmp)
    ans = list(product(*my_list))
    ansli = []
    print(ans)
    for i in ans:
        if len(frozenset(i)) == len(banned_id):
            # frozenset은 중복 제거 + 정렬까지함!
            ansli.append((frozenset(i)))
    print("---------------------------------")
    print(ansli)
    # 중복제거를 위한 set
    ansset = set(ansli)
    print(ansset)
    #set2 = {frozenset([2,4,5,1])}
    #print(set2)
    # len(set(list(frozenset(a) for a in product(*my_list) if len(frozenset(a)) == len(banned_id))))
    return len(ansset)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))