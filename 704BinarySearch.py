class Solution:
    """
    Returns the index of the given target in the given sorted list of numbers.
    
    :param nums: A sorted list of numbers.
    :type nums: List[int]
    :param target: The value to search for in the list.
    :type target: int
    :return: The index of the target value if found, -1 otherwise.
    :rtype: int
    """
    def search(self, nums, target: int) -> int:
        # Initialize two pointers to the start and end of the list
        left = 0
        right = len(nums) - 1

        # Loop until the two pointers meet
        while left <= right:
            # Calculate the middle index
            m = left + ((right - left) // 2)  

            # If the middle element is greater than the target, move the right pointer to the left
            if nums[m] > target:
                right = m - 1
            # If the middle element is less than the target, move the left pointer to the right
            elif nums[m] < target:
                left = m + 1
            # If the middle element is equal to the target, return its index
            else:
                return m
        
        # Return -1 if the target is not found
        return -1

import unittest

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_target_not_found(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_at_start(self):
        nums = [1, 2, 3, 4, 5]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_at_end(self):
        nums = [1, 2, 3, 4, 5]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_target_in_middle(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_empty_list(self):
        nums = []
        target = 1
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_list_with_duplicates(self):
        nums = [1, 2, 2, 3, 4, 4, 5]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 1)

    def test_list_with_negative_numbers(self):
        nums = [-5, -4, -3, -2, -1]
        target = -3
        self.assertEqual(self.solution.search(nums, target), 2)

if __name__ == '__main__':
    unittest.main()