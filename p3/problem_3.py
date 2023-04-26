def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left (list): The left sorted array.
        right (list): The right sorted array.

    Returns:
        list: The merged sorted array.
    """
    merged_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    merged_array += left[left_index:]
    merged_array += right[right_index:]

    return merged_array

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Return (0, 0) if the input_list is empty
    if not input_list:
        return 0, 0

    sorted_list = merge_sort(input_list)

    num1 = ""
    num2 = ""

    for value in sorted_list:
        # Append the digits to the numbers based on the parity
        if int(value) % 2 == 0:
            num1 += str(value)
        else:
            num2 += str(value)

    return int(num1), int(num2)


def test_function(test_case):
    """
    Tests the rearrange_digits function with the given test case.

    Args:
        test_case (tuple): A tuple containing the input list and expected output.

    Prints "Pass" if the test passes, "Fail" otherwise.
    """
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Case 1: Normal case
test_function([[1, 2, 3, 4, 5], [542, 31]])

# Test Case 3: Edge case - Empty input
test_function([[], (0, 0)])