#A method to append a value to a linked list

from hashlib import new


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def append_list(self, value):
  new_node = Node(value)
  #If statement test if the LL is empty
  if self.head is None:
    self.head = new_node
    self.tail = new_node
  else:
    self.tail.next = new_node
    self.tail = new_node
  self.length +=1
  return True