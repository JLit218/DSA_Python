##################   O(n^2 + n)   ###################
def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i,j)
    
  for k in range(n):
    print(k)

print_items(10)

#n would be a non-dominant, so it will be dropped  so this will still be a O(n^2) [+ n is dropped]