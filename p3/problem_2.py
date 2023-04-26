"""
Problem 2: Search in a Rotated Sorted Array

Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:

def rotated_array_search(input_list, number):
    
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    
   pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Initialize low and high pointers for binary search
    low = 0
    high = len(input_list) - 1

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2

        # If the mid element matches the target number, return the index
        if input_list[mid] == number:
            return mid

        # If the left side of the array is sorted
        if input_list[low] <= input_list[mid]:
            # If the target number is within the sorted left side, update high pointer
            if input_list[low] <= number < input_list[mid]:
                high = mid - 1
            else:
                # If the target number is not within the sorted left side, update low pointer
                low = mid + 1
        else:
            # If the target number is within the sorted right side, update low pointer
            if input_list[mid] < number <= input_list[high]:
                low = mid + 1
            else:
                # If the target number is not within the sorted right side, update high pointer
                high = mid - 1

    # If the target number is not found, return -1
    return -1


def linear_search(input_list, number):
    # Perform a linear search for the target number and return its index
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test cases for edge conditions

# Test Case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# Test Case 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Test Case 3
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# Test Case 4
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Test Case 5
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# Edge cases

# Edge Case 1: Edge case - Empty input list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# Edge Case 2: Edge case - Empty input list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Edge Case 3: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# Edge Case 4: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Edge Case 5: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge Case 6: Edge case - Empty input list
test_function([[], -1])

# Edge Case 7: Edge case - Single element
test_function([[7], 7])

# Edge Case 8: Edge case - Two elements
test_function([[5, 2], 2])

# Edge Case 9: Edge case - Large numbers
test_function([[23, 37, 42, 87, 91, 95, 99, 3, 8, 14], 8])

# Edge Case 10: Edge case - Target number not in the list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11])

# Edge Case 11: Edge case - list containing a single element and the target number not in the list
test_function([[1], 2])

# Edge Case 12: Edge case - target number smaller than the smallest number in the list
test_function([[6, 7, 8, 1, 2, 3, 4], 0])