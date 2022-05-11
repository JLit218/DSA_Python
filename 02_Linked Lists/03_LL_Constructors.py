#How to declare a class
#class LinkedList:
  #def __init__(self, value):
    #creates new node
  #def append(self, value):
    #creates new node
    #adds node to end
  #def prepend(self, value):
    #creates new node
    #adds node to beginning
  #def insert(self, index, value):  
    #creates new node
    #inserts node into desired index

#This would be redundant, instead create a class that creates node:

#Class that creates node
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
class LinkedList:
  #Initializes new linked list
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

#new linked list created by calling class and giving it the value of 4 
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
