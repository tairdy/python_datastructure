# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################

def remove_duplicates(lists):
    new_set = set()
    new_set.update(lists)
    print(new_set)

    # change set to list and return
    return list(new_set)


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""
