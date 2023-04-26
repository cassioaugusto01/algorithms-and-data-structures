def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
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
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort(input_list)

    num1 = ""
    num2 = ""

    for index, value in enumerate(sorted_list):
        if index % 2 == 0:
            num1 += str(value)
        else:
            num2 += str(value)

    return int(num1), int(num2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Case 1: Normal case
test_function([[1, 2, 3, 4, 5], [542, 31]])

# Test Case 2: Normal case
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test Case 3: Edge case - Empty input
test_function([[], (0, 0)])

# Test Case 4: Repeated numbers
test_function([[4, 4, 4, 4, 4, 4], [444, 444]])

# Test Case 5: Large numbers
test_function([[8, 23, 95, 47, 12, 34], [9532, 8741]])
