# Lessons 02 - 05 put together

# Creates class to creat new nodes #
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


my_linked_list = LinkedList(1)

my_linked_list.append_list(2)

my_linked_list.print_list()
