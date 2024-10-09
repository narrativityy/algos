# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

# Runtime: 593ms Beats 10.88% 
# Memory: 16.78MB Beats 98.24%

def findDifference(nums1, nums2):
    """
    Finds the difference of two arrays, nums1 and nums2.
    
    The result is a list of two lists. The first list contains all elements from nums1 that are not in nums2, and
    the second list contains all elements from nums2 that are not in nums1.
    
    :param nums1: The first array of numbers.
    :type nums1: list
    :param nums2: The second array of numbers.
    :type nums2: list
    :return: A list of two lists.
    :rtype: list
    """
    ans = []
    arr1_unique = []
    arr2_unique = []

    for val in nums1:
        if not val in nums2:
            if not val in arr1_unique:
                arr1_unique.append(val)

    for val in nums2:
        if not val in nums1:
            if not val in arr2_unique:
                arr2_unique.append(val)

    ans.append(arr1_unique)
    ans.append(arr2_unique)

    return ans

print(findDifference([1,2,3], [2,4,6]))
print(findDifference([1,2,3,3], [1,1,2,2]))