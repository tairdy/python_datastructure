# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################

def find_pairs(list1, list2, target):
    list_set = [target - i for i in list1]
    set1 = set(arr1)
    pairs = []
    for i in list1:
        pair_value = target - i
        if pair_value in list2:
            pairs.append((i, pair_value))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)


"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
