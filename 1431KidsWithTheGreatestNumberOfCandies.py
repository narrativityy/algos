def kidsWithCandies(candies, extraCandies):
    """
    Given the array candies and the integer extraCandies, where candies[i] represents the number of candies the ith kid has.
    For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
    Notice that multiple kids can have the greatest number of candies.

    :param candies: The list of integers where candies[i] is the number of candies the ith kid has.
    :type candies: List[int]
    :param extraCandies: The number of extra candies that can be distributed.
    :type extraCandies: int
    :return: A boolean array where res[i] is True if the ith kid can have the greatest number of candies after distributing extraCandies.
    :rtype: List[bool]
    """
    result = []
    max_candies = max(candies)

    # Iterate over each kid
    for count in candies:
        # Check if the kid can have the greatest number of candies after distributing extraCandies
        result.append(count + extraCandies >= max_candies)

    return result

print(kidsWithCandies([2,3,5,1,3], 3))