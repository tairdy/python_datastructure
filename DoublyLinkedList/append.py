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
            new_node.prev = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


new_list = DoublyLinkedList(4)
new_list.append(5)

new_list.print()
