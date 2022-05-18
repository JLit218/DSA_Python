# In a binary search tree, greater numbers go on the right branch, while lesser numbers go on the left branch
# continues down the tree
# everything to the right is greater than, left is less than
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
