# Recursion - A function that calls itself... until it doesn't

# Pseudocode Example #

# def open_gift_box():
#    if ball:
#        return ball
#     open_gift_box()

# The process of opening each new box is the same
# Each time we open a box, we make this problem smaller (boxes keep getting smaller ).
# return causes the function to stop
# the "ball" is called a base case
# if it's another "box" it is a recursive case
# must have a base case or the recursive case will call infinitely (a stack overflow)
# must have a return statement to stop code

######### Call Stack ############
# uses a stack of recursive function
# one function is called and then removed from the stack, the next function is called and removed from the stack. So on, and so on.

# EX
def funcThree():
    print('Three')


def funcTwo():
    funcThree()
    print('Two')


def funcOne():
    funcTwo()
    print('One')


funcOne()


######### Factorial ############
# 4! = 4 * 3 * 2 * 1
#   4 * 3!
#       3 * 2!
#           2 * 1!
#               1
# 1 would be the base case

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
