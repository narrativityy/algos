def uniqueOccurrences(arr: list[int]) -> bool:
    """
    Return True if all the values in the given array have unique number of occurrences, and False otherwise.

    :param arr: The list of integers
    :return: True if all the values in the given array have unique number of occurrences, and False otherwise
    """
    freq_map = {}

    for val in arr:
        if val in freq_map:
            freq_map[val] += 1
        else:
            freq_map[val] = 1

    arr = []

    for val in freq_map:
        if freq_map[val] in arr:
            return False
        else:
            arr.append(freq_map[val])

    return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))