class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if the given string is a palindrome, and False otherwise.
        
        A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
        
        :param s: The string to check for being a palindrome.
        :type s: str
        :return: True if the string is a palindrome, False otherwise.
        :rtype: bool
        """
        # Create a new string that contains only alphanumeric characters in lowercase
        filtered_str = ""

        for c in s:
            if c.isalnum():
                filtered_str += c.lower()
        
        # Initialize two pointers to point to the start and end of the string
        leftInd = 0
        rightInd = len(filtered_str) - 1

        # Iterate over the string and compare the characters at the left and right pointers
        while leftInd <= rightInd:
            if(filtered_str[leftInd] == filtered_str[rightInd]):
                leftInd += 1
                rightInd -= 1
            else:
                # If the characters do not match, the string is not a palindrome
                return False

        # If the loop completes and the characters matched, then the string is a palindrome
        return True

import unittest

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))

    def test_string_with_spaces(self):
        self.assertTrue(self.solution.isPalindrome("   "))

    def test_string_with_punctuation(self):
        self.assertTrue(self.solution.isPalindrome(".,.'"))

    def test_string_with_capitalization(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal. Panama!"))

if __name__ == '__main__':
    unittest.main()