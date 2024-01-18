class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.prev = new_node
        self.length = 1

    def append(self, value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
            return temp
