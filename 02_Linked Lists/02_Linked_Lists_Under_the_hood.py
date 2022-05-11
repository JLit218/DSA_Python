#each node in a linked list is essentially a dictionary

#head: {
  # "value": 7,
  # "next": {
    #####this would be the tail#####
            # "value": 4,
            # "next": None 
            # }
# }

#example

from operator import ne

#############THIS IS A DICTIONARY, but this is essentially how a linked list works##############

head = {
  "value": 11,
  "next": {
    "value": 3,
    "next": {
      "value": 23,
      "next": {
        "value": 7,
        "next": None
      }
    }
  }
}

print(head['next']['next']['value'])

#how to run this as an actual linked list
#print(my_linked_list.head.next.next.value)