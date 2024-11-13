class Solution:
    def containsDuplicate(self, nums) -> bool:
        """
        Determines if any value appears at least twice in the array.
        
        :param nums: List of integers to check for duplicates.
        :return: True if any value appears at least twice, False otherwise.
        """
        freqMap = {}

        # Iterate over each number in the list
        for num in nums:
            # If the number is not in the frequency map, add it
            if num not in freqMap:
                freqMap[num] = 1
            else:
                # If the number is already in the frequency map, a duplicate is found
                return True
        
        # Return False if no duplicates are found
        return False

import unittest

class TestContainsDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(Solution().containsDuplicate([]))

    def test_unique_elements(self):
        self.assertFalse(Solution().containsDuplicate([1, 2, 3, 4, 5]))

    def test_duplicate_elements(self):
        self.assertTrue(Solution().containsDuplicate([1, 2, 2, 3, 4]))

    def test_multiple_duplicate_elements(self):
        self.assertTrue(Solution().containsDuplicate([1, 2, 2, 3, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(Solution().containsDuplicate([-1, -2, -2, -3, -4]))

    def test_zero(self):
        self.assertTrue(Solution().containsDuplicate([0, 0, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()