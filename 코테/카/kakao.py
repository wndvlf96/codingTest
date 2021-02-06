from itertools import permutations
str = "qweewq"
list1 = []
for i in str:
    list1.append(i)
list2 = list(map(''.join, permutations(list1, 2)))
print(list2)