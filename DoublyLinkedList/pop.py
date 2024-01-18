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
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp

        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_doublylinkedlist = DoublyLinkedList(3)
my_doublylinkedlist.append(4)

my_doublylinkedlist.print_list()


print("popping one node from the end")
my_doublylinkedlist.pop()
my_doublylinkedlist.print_list()

print("popping another node, this time only one node")
my_doublylinkedlist.pop()
