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
# Removes Node from end of LL #

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

# Prepend Method #
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# Pop first Method #
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # Get method #
    def get(self, index):
      # tests if index value is valid
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # the _ replaces "i", if "i" is not used in for loop
        for _ in range(index):
            temp = temp.next
        return temp

    # Set method #
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


my_linked_list = LinkedList(11)
my_linked_list.append_list(3)
my_linked_list.append_list(23)
my_linked_list.append_list(7)

my_linked_list.set_value(1, 4)

my_linked_list.print_list()
