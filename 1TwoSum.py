def twoSum(nums, target):
    """
    Finds two elements in the given list that add up to the given target value.
    
    :param nums: The list of numbers to search in.
    :type nums: List[int]
    :param target: The target value that the two numbers should add up to.
    :type target: int
    :return: A list of two indices of the two numbers that add up to the target value.
    :rtype: List[int]
    """
    # Keep track of the index and the value
    index = 0
    # A dictionary to keep track of all the numbers we have seen so far
    matches = {}
    # Iterate over the list of numbers
    for num in nums:
        # Calculate the value that we need to add up to the target
        match = target - num
        # If the value is already in our dictionary, then we have found the two numbers
        if match in matches:
            # Return the indices of the two numbers
            return [matches[match], index]
        else:
            # Otherwise, add the current number and index to the dictionary
            matches[num] = index
        # Increment the index
        index += 1
    # If we have not found two numbers that add up to the target, then return an empty list
    return []

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))