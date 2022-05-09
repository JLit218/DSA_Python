##################   O(n^2)   ###################
def print_items(n):
  for i in range(n):
    for j in range(n):
      #n * n aka n^2
      for k in range(n):
        print(i,j,k)
      #n * n * n aka n^3 (regardless how many exponents this will be simplified to O(n^2)

print_items(10)

############O(n^2) is a loop within a loop