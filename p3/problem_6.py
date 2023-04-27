"""
Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

def get_min_max(ints):
   
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    
   pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints (list): list of integers containing one or more integers
    """
    if not ints:
        return None

    min_val = ints[0]
    max_val = ints[0]

    # Iterate through the list to find the min and max values
    for num in ints:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)


# Example Test Case of Ten Integers
import random


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Test Case 1: Normal case
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 2: Edge case - Empty input
print("Pass" if (None == get_min_max([])) else "Fail")

# Test Case 3: Negative numbers
l = [i for i in range(-10, 0)]  # a list containing -10 to -1
random.shuffle(l)
print("Pass" if ((-10, -1) == get_min_max(l)) else "Fail")

# Test Case 4: Large numbers
l = [i for i in range(1000, 1010)]  # a list containing 1000 - 1009
random.shuffle(l)
print("Pass" if ((1000, 1009) == get_min_max(l)) else "Fail")

# Test Case 5: Edge case - Single element
print("Pass" if ((5, 5) == get_min_max([5])) else "Fail")

# Test Case 6: Edge case - All elements are the same
print("Pass" if ((7, 7) == get_min_max([7, 7, 7, 7])) else "Fail")
