class Solution:
    def maxArea(self, height) -> int:
        """
        Returns the maximum area that can be obtained by pouring water into
        a container of a given height.

        Parameters
        ----------
        height : List[int]
            The height of the container.

        Returns
        -------
        int
            The maximum area that can be obtained.
        """
        # Initialize max_val to 0
        max_val = 0
        # Initialize the left and right pointers to the start and end of the list
        left = 0
        right = len(height) - 1

        # Loop until the two pointers meet
        while left < right:
            # Check if the height of the left pointer is greater than the height of the right pointer
            if height[left] > height[right]:
                # Calculate the area of the container for the right pointer
                temp_val = height[right] * (right - left)
                # Move the right pointer to the left
                right -= 1
            else:
                # Calculate the area of the container for the left pointer
                temp_val = height[left] * (right - left)
                # Move the left pointer to the right
                left += 1
            # Check if the current area is greater than the max_val
            if temp_val > max_val: 
                # Update max_val if the current area is greater
                max_val = temp_val

        # Return the maximum area
        return max_val


import unittest

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_equal_heights(self):
        height = [1, 1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_unequal_heights(self):
        height = [1, 2]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_multiple_lines(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_single_line(self):
        height = [1]
        self.assertEqual(self.solution.maxArea(height), 0)

    def test_empty_list(self):
        height = []
        self.assertEqual(self.solution.maxArea(height), 0)

    def test_list_of_zeros(self):
        height = [0, 0, 0]
        self.assertEqual(self.solution.maxArea(height), 0)

if __name__ == '__main__':
    unittest.main()