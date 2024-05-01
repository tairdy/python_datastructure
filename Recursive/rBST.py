
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def insert(self, value):
    #     new_node = Node(value)
    #     if self.root is None:
    #         self.root = new_node
    #         return True
    #     temp = self.root
    #     while (True):
    #         if new_node.value == temp.value:
    #             return False
    #         if new_node.value < temp.value:
    #             if temp.left is None:
    #                 temp.left = new_node
    #                 return True
    #             temp = temp.left
    #         else:
    #             if temp.right is None:
    #                 temp.right = new_node
    #                 return True
    #             temp = temp.right

    ## WRITE R_CONTAINS METHODS HERE ##
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            new_node = Node(value)
            return new_node
        elif value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)
        if current_node.value < value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
