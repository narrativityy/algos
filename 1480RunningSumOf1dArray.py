class Solution:
    def runningSum(self, nums):
        j = 0
        s = 0
        while(j < len(nums)):
            s = s + nums[j]
            nums[j] = s
            j += 1
        return nums

import unittest

class TestRunningSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.runningSum([]), [])

    def test_single_element_list(self):
        self.assertEqual(self.solution.runningSum([1]), [1])

    def test_multiple_element_list_positive(self):
        self.assertEqual(self.solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_multiple_element_list_negative(self):
        self.assertEqual(self.solution.runningSum([-1, -2, -3, -4]), [-1, -3, -6, -10])

    def test_multiple_element_list_mixed(self):
        self.assertEqual(self.solution.runningSum([1, -2, 3, -4]), [1, -1, 2, -2])

if __name__ == '__main__':
    unittest.main()