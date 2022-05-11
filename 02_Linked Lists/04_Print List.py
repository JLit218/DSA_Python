#The following method prints all values within a list

def print_list(self):
  temp = self.head
  while temp is not None:
    print(temp.value)
    temp = temp.next