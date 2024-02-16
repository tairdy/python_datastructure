def item_in_common(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
        print(i)
    print(dict)
    for j in list2:
        if j in dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))
