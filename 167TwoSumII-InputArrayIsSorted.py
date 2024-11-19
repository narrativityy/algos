class Solution:
    def twoSum(self, numbers, target: int):
        """
        Finds two numbers in a sorted list that add up to a specific target.

        :param numbers: A sorted list of integers.
        :param target: The target sum.
        :return: A list containing the indices (1-based) of the two numbers that add up to the target.
        """
        leftInd = 0  # Initialize the left pointer
        rightInd = len(numbers) - 1  # Initialize the right pointer

        # Loop until the two pointers meet
        while leftInd <= rightInd:
            current_sum = numbers[leftInd] + numbers[rightInd]
            if current_sum == target:
                # If the sum of the two numbers is equal to the target, return their indices
                return [leftInd + 1, rightInd + 1]
            elif current_sum > target:
                # If the sum is greater than the target, move the right pointer to the left
                rightInd -= 1
            else:
                # If the sum is less than the target, move the left pointer to the right
                leftInd += 1


import unittest

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_input_with_solution(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_valid_input_without_solution(self):
        numbers = [2, 7, 11, 15]
        target = 10
        expected = None
        self.assertIsNone(self.solution.twoSum(numbers, target))

    def test_empty_list(self):
        numbers = []
        target = 9
        expected = None
        self.assertIsNone(self.solution.twoSum(numbers, target))

    def test_list_with_duplicate_elements(self):
        numbers = [2, 2, 11, 15]
        target = 4
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_list_with_negative_numbers(self):
        numbers = [-2, -7, 11, 15]
        target = -9
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_list_with_zero(self):
        numbers = [0, 7, 11, 15]
        target = 7
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

if __name__ == '__main__':
    unittest.main()