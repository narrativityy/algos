class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        partitions = round(len(s) / 2)
        subpartitions = []

        for i in range(0, partitions):
            subpartitions.append(s[i * 2: i * 2 + 2])

        for partition in subpartitions:
            if partition[0] is not partition[1]:
                count += 1

        return count

import unittest

class TestMinChanges(unittest.TestCase):
    def test_even_length_identical_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("aaaa"), 0)

    def test_even_length_different_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("abcd"), 2)

    def test_odd_length_identical_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("aaaaa"), 0)

    def test_odd_length_different_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("abcde"), 2)

    def test_alternating_identical_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("ababab"), 3)

    def test_two_identical_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("aa"), 0)

    def test_two_different_characters(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("ab"), 1)

if __name__ == '__main__':
    unittest.main()