# The trunk is 2^1 or 1 step
# next branch is 2^2 or 2 setps
# next branch is 2^3 or 3 steps
# and so on
# This means that any methods using a binary search tree are O(log n)[DIVIDE AND CONQUER], almsot as efficient as O(1)
# If the tree does not fork then it is essentially a linked list, and searching through is now O(n)

# Binary Search Tree is better for lookup(), and remove() (by better I mean quicker space/time complexity)
# LL is better for inset() it is O(1)
