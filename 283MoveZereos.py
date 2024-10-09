import unittest
def moveZeroes(nums) -> None:
    """
    Moves all zeros to the right of the array, and all non-zero elements to the left.
    The relative order of the elements is preserved.
    """
    # The index of the first zero element
    left = 0

    # Iterate over the array
    for right in range(len(nums)):
        # If the current element is not zero, swap it with the left element
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            # Increment the left index
            left += 1

class TestMoveZeroes(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        moveZeroes(nums)
        self.assertEqual(nums, [])

    def test_no_zeros(self):
        nums = [1, 2, 3, 4, 5]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_only_zeros(self):
        nums = [0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0])

    def test_zeros_at_beginning(self):
        nums = [0, 0, 1, 2, 3]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_zeros_in_middle(self):
        nums = [1, 2, 0, 0, 3, 4]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0, 0])

    def test_zeros_at_end(self):
        nums = [1, 2, 3, 4, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0, 0])

    def test_multiple_zeros(self):
        nums = [0, 1, 0, 2, 0, 3, 0, 4]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0, 0, 0, 0])

    def test_negative_numbers_and_zeros(self):
        nums = [-1, 0, -2, 0, 3, 0, -4]
        moveZeroes(nums)
        self.assertEqual(nums, [-1, -2, 3, -4, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()