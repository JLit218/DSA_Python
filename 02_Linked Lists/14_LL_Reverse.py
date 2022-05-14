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

    # Insert Method #
    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_list(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Remove Method #
    def remove_value(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Reverse Method #
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        # for loop MUST be in this order to not break the link. See Lecture 32 on Udemy


my_linked_list = LinkedList(1)
my_linked_list.append_list(2)
my_linked_list.append_list(3)
my_linked_list.append_list(4)

my_linked_list.reverse()

my_linked_list.print_list()
