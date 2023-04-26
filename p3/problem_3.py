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
def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list += left[left_index:]
    merged_list += right[right_index:]

    return merged_list


def rearrange_digits(input_list):
    if len(input_list) < 2:
        return input_list

    sorted_list = merge_sort(input_list)
    num1, num2 = '', ''

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 += str(sorted_list[i])
        else:
            num2 += str(sorted_list[i])

    return int(num1), int(num2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test Case 1: Regular case
test_function([[1, 2, 3, 4, 5], [542, 31]])

# Test Case 2: Regular case
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test Case 3: Edge case - Empty input list
test_function([[], []])

# Test Case 4: Edge case - Single element
test_function([[7], [7]])

# Test Case 5: Edge case - Two elements
test_function([[5, 2], [5, 2]])

# Test Case 6: Edge case - All elements are the same
test_function([[7, 7, 7, 7, 7, 7, 7], [7777, 777]])

# Test Case 7: Edge case - Large numbers
test_function([[9, 5, 8, 6, 7, 3, 2, 1, 0, 4], [97531, 86420]])
