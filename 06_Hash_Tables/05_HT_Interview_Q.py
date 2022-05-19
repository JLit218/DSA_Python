# find the number in common with list1 [1,3,5] and list2[2,4,5] using O(n)
# first thought is to typically just do a nested loop, however this is O(n^2)

############# Inefficient solution O(n^2) #############
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

########## Efficient solution O(n) ###############


def efficient_item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

# O(n^2)
print(item_in_common(list1, list2))

# O(n)
print(efficient_item_in_common(list1, list2))
