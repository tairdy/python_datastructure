list = [1, 2, 3]
x = 5
if x in list:

    print(x)
else:
    print("error")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(10)
node2 = Node(15)
node3 = Node(5)
prev = None
prev = node1
prev.next = node2
node2.next = node3


print(prev.value)
print(prev.next.value)
print(prev.next.next.value)
