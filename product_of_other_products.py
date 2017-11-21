import doctest

def prod_of_others(nums):
    """
    You have a list of integers, and for each index you want to 
    find the product of every integer except the integer at that index.

        >>>prod_of_others([4])
        IndexError: array should be at least 2 numbers

        >>>prod_of_others([3, 4, 9, 2])
        [72, 54, 24, 108]

    """
    

    if len(nums) < 2:
        raise IndexError('array should be at least 2 numbers')
    
    new_arr = [None] * len(nums)
    
    prod_at_index = 1
    i = 0
    while i < len(nums):
        new_arr[i] = prod_at_index
        prod_at_index *= nums[i]
        i += 1
    
    prod_at_index = 1
    i = len(nums) - 1
    while i >= 0:
        new_arr[i] *= prod_at_index
        prod_at_index *= nums[i]
        i -= 1
    
    return new_arr


print prod_of_others([8, 10, 2])
print prod_of_others([2, 3, 4, 7])
print prod_of_others([3])
print prod_of_others([3, 4, 9, 2])
