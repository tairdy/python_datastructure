# DLL: Reverse ( ** Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.
# 
# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.
# 
# Do not change the value of any of the nodes.
# 
# Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.
# 
# Pseudo-code can be found under "Hints" (above).




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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    ## WRITE REVERSE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################
    def reverse(self):
        if self.length <= 0:
            return False
        elif self.length ==1:
            pass
        elif self.length == 2:
            
            temp_head = self.head
            temp_tail = self.tail
            
            temp_head.prev = temp.tail
            temp_head.next = None

            temp_tail.prev = None
            temp_tail.next = temp.head

            self.head = temp_tail
            self.tail = temp_head
           
        else:

            temp_head = self.head
            temp_tail= self.tail
            
            print("processing")
            temp_head_next = temp_head.next
            temp_tail_prev = temp_tail.prev
            print(f"temp_head value = {temp_head.value}")
            print(f"temp_tail value = {temp_tail.value}")

            print(f"temp_head_next value = {temp_head_next.value}")
            print(f"temp_tail_prev value = {temp_tail_prev.value}")

            print(f"temp_tail_prev.next = {temp_tail_prev.next.value}")

            temp_head.prev = temp_tail_prev
            temp_head.next = None
            temp_tail_prev.next = temp_head

            temp_tail.prev = None
            temp_tail.next = temp_head_next
            temp_head_next.prev = temp_tail
            
            final_head = temp_tail
            final_tail = temp_head
            count = 1 
            for _ in range(int(self.length / 2 - 1)):
                print(f"count = {count}")
                count += 1
                
                tmp = temp_head
                temp_head = temp_tail.next
                temp_tail = tmp.prev
                
                print(f"temp_head value start = {temp_head.value}")
                print(f"temp_tail value start = {temp_tail.value}")
                temp_head_next = temp_head.next
                temp_head_prev = temp_head.prev
                
                temp_tail_next = temp_tail.next
                temp_tail_prev = temp_tail.prev
                print(f"temp_tail_prev value start = {temp_tail_prev.value}")

                temp_head.prev = temp_tail.prev
                temp_head.next = temp_tail_next
                temp_tail_prev.next = temp_head
                temp_tail_next.prev = temp_head

                temp_tail.prev = temp_head_prev
                temp_tail.next = temp_head_next
                temp_head_prev.next = temp_tail
                temp_head_next.prev = temp_tail
                
                temp_head = temp_tail.next
                temp_tail = temp_head.prev
                print(f"temp_head after = {temp_head.value}")
                print(f"temp_tail after = {temp_tail.value}")

            self.head = final_head
            self.tail = final_tail
             
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""

