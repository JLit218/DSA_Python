##################   n2   ###################
def print_items(n):
  for i in range(n):
    print(i)

  for j in range(n):
    print(j)

print_items(10)
#Outputs 0-9 for each for loop
#Ran n + n times, would be O(2n), but we drop constants so it would be O(n)