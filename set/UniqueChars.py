# WRITE HAS_UNIQUE_CHARS FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################

def has_unique_chars(string):
    new_set = set(string)
    # print(string, new_set)
    # print(f"length of string = {len(string)}")
    if len(string) == len(new_set):
        return True
    return False


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""
