class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print(self):
        tmp = self.head

        while tmp is not None:
            print(f"showing value {tmp.value}")
            tmp = tmp.next


list = LinkedList(5)
list.append(3)
list.print()
