"""
Problem 1: Square Root of an Integer

Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

def sqrt(number):
    
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
"""
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # If the number is 0 or 1, return the number itself
    if number == 0 or number == 1:
        return number

    # Initialize start, end, and result variables for binary search
    start = 1
    end = number
    result = 0

    # Perform binary search to find the square root
    while start <= end:
        # Calculate the middle value
        mid = (start + end) // 2

        # If mid^2 equals the number, return mid as the square root
        if mid * mid == number:
            return mid

        # If mid^2 is less than the number, update start and store mid as the result
        if mid * mid < number:
            start = mid + 1
            result = mid
        else:
            # If mid^2 is greater than the number, update end
            end = mid - 1

    # Return the final result, which is the floored square root
    return result

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")  # Test a perfect square
print("Pass" if (0 == sqrt(0)) else "Fail")  # Test with zero
print("Pass" if (4 == sqrt(16)) else "Fail")  # Test another perfect square
print("Pass" if (1 == sqrt(1)) else "Fail")  # Test with one
print("Pass" if (5 == sqrt(28)) else "Fail")  # Test a non-square number

# Edge cases
print("Pass" if (999 == sqrt(998001)) else "Fail")  # Test a large non-square number
print("Pass" if (46340 == sqrt(2147483647)) else "Fail")  # Test the largest possible 32-bit integer
print("Pass" if (2 == sqrt(5)) else "Fail")  # Test the smallest non-square number greater than 1
print("Pass" if (31622 == sqrt(1000000000)) else "Fail")  # Test a large square number with a round square root
print("Pass" if (1 == sqrt(2)) else "Fail")  # Test the smallest non-square number
