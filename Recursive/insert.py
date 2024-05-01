def __r_insert(self, current_node, value):
    if current_node == None:
        return Node(value)
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node, value)
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node, value)
    return current_node


def r_insert(self, value):
    if self.root == None:
        self.root = Node(value)
    self.__r_insert(self.root, value)
