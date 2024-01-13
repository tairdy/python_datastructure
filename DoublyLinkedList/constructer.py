class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
