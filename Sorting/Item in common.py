#Different approaches to find an item in common

def approach1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def approach2(list1, list2):
    mydict = {}
    for i in list1:
        mydict[i] = True
    for j in list2:
        if j in mydict:
            return True
    return False

list1 = [6,7,8]
list2 = [1,3,8]

print(approach1(list1, list2))
print(approach2(list1, list2))
