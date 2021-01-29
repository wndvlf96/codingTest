ans = []
while True:
    stk = []
    in1 = input()
    if in1 == ".":
        break
    for i in in1:
        if i == "(" or i =="[":
            stk.append(i)
        elif i ==")":
            if len(stk)==0:
                stk.append(i)
                break
            elif stk[-1] == "(":
                del stk[-1]
            else:
                stk.append(i)
                break
        elif i =="]":
            if len(stk)==0:
                stk.append(i)
                break
            elif stk[-1] == "[":
                del stk[-1]
            else:
                stk.append(i)
                break
        elif i == ".":
            break
    if stk==[]:
        ans.append("yes")
    else:
        ans.append("no")

for i in ans:
    print(i)