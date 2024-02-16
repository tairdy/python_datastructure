
# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################

def find_duplicates(list):
    dict = {}
    duplicate_list = []
    for i in list:
        # print(f"list data = {i}")
        # print(f"dict(i) = {dict.get(i)}")
        if dict.get(i) is None:
            dict[i] = False
        else:
            dict[i] = True

    # print(dict)
    for j in dict:
        if dict[j] == True:
            duplicate_list.append(j)
    return duplicate_list


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
