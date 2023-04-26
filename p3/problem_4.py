"""
Problem 4: Dutch National Flag Problem
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

def sort_012(input_list):
    
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list (list): List to be sorted
       
    Returns:
       list: Sorted array
    """
    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Case 1: Regular case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# Test Case 2: Regular case
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# Test Case 3: Regular case
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test Case 4: Edge case - Empty input_list
test_function([])

# Test Case 5: Edge case - All elements are the same
test_function([1, 1, 1, 1, 1, 1])

"""
input_lists with 1000 and 10000 elements, respectively. 
The elements are randomly chosen from 0, 1, and 2. 
"""

import random

# Test Case 6: Edge case - Large input_list with 1000 elements
large_input_list = [random.choice([0, 1, 2]) for _ in range(1000)]
test_function(large_input_list)

# Test Case 7: Edge case - Large input_list with 10000 elements
large_input_list = [random.choice([0, 1, 2]) for _ in range(10000)]
test_function(large_input_list)
