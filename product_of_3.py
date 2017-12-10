def highest_prod(nums):
    """
    highest product of 3 integers from given list of ints
    
    >>> highest_prod([-10, -10, 1, 3, 2])
    300
    
    >>> highest_prod([1, 10, -5, 1, -100])
    5000
    
    >>> highest_prod([1, 10, 5, 1, 100])
    5000
    
    """
    
    nums.sort()
    
    # ACCOUNT FOR NEGATIVE NUMBERS
    if nums[0] < 0 and nums[1] < 0:
        return abs(nums[0]) * abs(nums[1]) * nums[-1]
    else: 
    # THIS METHOD DOES NOT ACCOUNT FOR NEGATIVE NUMBERS
        return nums[-1]*nums[-2]*nums[-3]

# print highest_prod([-10, -10, 1, 3, 2])
# print highest_prod([1, 10, -5, 1, -100])
# print highest_prod([1, 10, 5, 1, 100])


if __name__ == "__main__":
    import doctest
    doctest.testmod()