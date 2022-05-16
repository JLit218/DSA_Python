# Think of a Queue as the people in a line or a queue in spotify. You add on one end and subtract from the other
# one person leaves the line from the front, one person enters the line from behind

# Queue as a linked List #
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = Queue(4)

my_queue.print_queue()
