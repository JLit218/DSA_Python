#appending another note to a list makes a new tail
#this is also O(1), adding/removing a new head is the same

#removing a node from the tail (.pop) requires iterating through the list to get to the pointer that points to the new tail O(n)

#adding/Removing a node in the middle:
#new node must first point to the note after, then the node prior to the new node must point to the new node, O(n)

#searching through an index O(n)