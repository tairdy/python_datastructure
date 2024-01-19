class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        if self.length == 0:
            new_node = Node(value)
            self.head = None
            self.tail = None
            self.length += 1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        elif index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
            return temp

    def set_value(self, index, value):

        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.get(index)
            temp.value = value
            return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1, 4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    DLL before set_value():
    11
    3
    23
    7

    DLL after set_value():
    11
    4
    23
    7

"""
