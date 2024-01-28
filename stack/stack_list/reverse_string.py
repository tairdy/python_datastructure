

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
#########################################

def reverse_string(input_string):
    stack = Stack()

    if len(input_string) == 0:
        return ""
    elif len(input_string) == 1:
        return input_string
    else:
        tmp_string = ""
    for i in input_string:
        stack.push(i)
        # print(stack.stack_list)
    for _ in input_string:
        tmp_string += stack.pop()
    return tmp_string


my_string = 'hello'

print(reverse_string(my_string))


"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
