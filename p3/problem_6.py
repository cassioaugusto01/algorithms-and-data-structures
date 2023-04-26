def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None

    min_val = ints[0]
    max_val = ints[0]

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
