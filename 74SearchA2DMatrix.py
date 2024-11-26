class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """
        Searches for a target value in a 2D matrix. This matrix has the properties
        that each row is sorted in ascending order, and the first integer of each row 
        is greater than the last integer of the previous row.

        :param matrix: A list of lists of integers, where each sublist is sorted.
        :param target: The integer value to search for in the matrix.
        :return: True if the target is found, False otherwise.
        """
        top = 0
        bottom = len(matrix) - 1

        # Perform binary search on the rows
        while top <= bottom:
            middle = top + ((bottom - top) // 2)
            left = 0
            right = len(matrix[middle]) - 1

            # Perform binary search on the columns of the current row
            while left <= right:
                m = left + ((right - left) // 2)
                if matrix[middle][m] > target:
                    right = m - 1
                elif matrix[middle][m] < target:
                    left = m + 1
                else:
                    return True
            
            # Adjust the search range based on the comparison
            if matrix[middle][m] > target:
                bottom = middle - 1
            elif matrix[middle][m] < target:
                top = middle + 1
            
        # Return False if the target is not found
        return False

import unittest

class TestSearchMatrix(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_target_in_first_row(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 1
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_in_last_row(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 50
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_in_middle_row(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 16
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_not_in_matrix(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 25
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_matrix_has_one_row(self):
        matrix = [
            [1, 3, 5, 7]
        ]
        target = 5
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_matrix_has_one_column(self):
        matrix = [
            [1],
            [10],
            [23]
        ]
        target = 10
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_matrix_is_empty(self):
        matrix = []
        target = 5
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_target_is_duplicate(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 10
        self.assertTrue(self.solution.searchMatrix(matrix, target))

if __name__ == '__main__':
    unittest.main()