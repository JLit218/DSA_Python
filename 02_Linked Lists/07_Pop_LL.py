# Removing a node from a LL
# using pre and temp as new values to help move the tail backwards


################## Previous Code #################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creates and contains all LL Methods #


class LinkedList:
    # Initializes new linked list #
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Prints the entire LL #
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Adds value to the end of LL #
    def append_list(self, value):
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

################ Pop Method ####################

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append_list(2)

# my_linked_list.print_list()

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item = Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())
