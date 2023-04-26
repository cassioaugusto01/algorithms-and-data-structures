"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).


Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


Boilerplate:

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

def find_pivot(input_list, low, high):
    """
    Find the pivot element in the rotated sorted array.
    
    Args:
        input_list (list): Rotated sorted array.
        low (int): Starting index for the search.
        high (int): Ending index for the search.
        
    Returns:
        int: Pivot index, or -1 if not found.
    """
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2

    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid
    if mid > low and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[low] >= input_list[mid]:
        return find_pivot(input_list, low, mid - 1)
    else:
        return find_pivot(input_list, mid + 1, high)


def binary_search(input_list, low, high, number):
    """
    Perform a binary search on a sorted array.
    
    Args:
        input_list (list): Sorted array.
        low (int): Starting index for the search.
        high (int): Ending index for the search.
        number (int): Target number to search for.
        
    Returns:
        int: Index of the target number if found, or -1 if not found.
    """
    if high < low:
        return -1

    mid = (low + high) // 2
    if number == input_list[mid]:
        return mid
    if number > input_list[mid]:
        return binary_search(input_list, mid + 1, high, number)
    else:
        return binary_search(input_list, low, mid - 1, number)


def rotated_array_search(input_list, number):
    """
    Find the index of the target number in a rotated sorted array.
    
    Args:
        input_list (list): Rotated sorted array.
        number (int): Target number to search for.
        
    Returns:
        int: Index of the target number if found, or -1 if not found.
    """
    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)

    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)
    else:
        return binary_search(input_list, pivot + 1, len(input_list) - 1, number)


def linear_search(input_list, number):
    """
    Perform a linear search on an array.
    
    Args:
        input_list (list): Array to search.
        number (int): Target number to search for.
        
    Returns:
        int: Index of the target number if found, or -1 if not found.
    """
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

# Test Case 1: Edge case - Empty input list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# Test Case 2: Edge case - Empty input list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Test Case 3: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# Test Case 4: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Test Case 5: Edge case - Empty input list
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test Case 6: Edge case - Empty input list
test_function([[], -1])

# Test Case 7: Edge case - Single element
test_function([[7], 7])

# Test Case 8: Edge case - Two elements
test_function([[5, 2], 2])

# Test Case 9: Edge case - Large numbers
test_function([[23, 37, 42, 87, 91, 95, 99, 3, 8, 14], 8])

# Test Case 10: Edge case - Target not in input_list
test_function([[6, 7, 8, 1, 2, 3, 4], 50])

# Test Case 11: Edge case - All elements are the same
test_function([[7, 7, 7, 7, 7, 7, 7], 7])
