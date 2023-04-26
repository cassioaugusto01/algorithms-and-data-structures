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


# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge cases
test_function([[], 3])  # Test with an empty list
test_function([[1], 1])  # Test with a list containing a single element
test_function([[1], 2])  # Test with a list containing a single element and the target number not in the list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11])  # Test with a target number not in the list
test_function([[6, 7, 8, 1, 2, 3, 4], 0])  # Test with a target number smaller than the smallest number in the list
