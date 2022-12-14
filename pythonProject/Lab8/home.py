'''# define the functions for the basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# take input from the user for the operation and operands
operation = input("What operation would you like to perform (+, -, *, /)? ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))'''



'''# perform the operation
if operation == '+':
    print(num1, "+", num2, "=", add(num1, num2))

elif operation == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif operation == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif operation == '/':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid operator")'''


'''def find(list, value):
    # create an empty list to store the indices
    indices = []

    # iterate through the list and find the value
    for i in range(len(list)):
        if list[i] == value:
            indices.append(i)

    # return the list of indices
    return indices


# test the function with a sample list and value
my_list = [1, 2, 3, 4, 5, 2, 6, 7, 2, 8]
value = 2
indices = find(my_list, value)
print(indices)  # [1, 5, 8]'''


'''import numpy as np

# create an ndarray of size 5x5 filled with zeros
arr = np.zeros((5, 5))
print(arr)

# replace the zeros on the edges with ones
arr[0, :] = 1  # top edge
arr[:, 0] = 1  # left edge
arr[-1, :] = 1  # bottom edge
arr[:, -1] = 1  # right edge
print(arr)


# define a function to swap zeros and ones
def swap(arr):
    # create a copy of the array
    new_arr = arr.copy()

    # swap zeros and ones
    new_arr[arr == 0] = 1
    new_arr[arr == 1] = 0

    # return the new array
    return new_arr


# test the swap function
swapped = swap(arr)
print(swapped)'''

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
