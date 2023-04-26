"""
Problem 3: Rearrange Array Digits

Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:

def rearrange_digits(input_list):
    
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
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
