class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if the given string of parentheses is valid by using a stack.

        A valid string of parentheses is a string where every open parenthesis has a
        corresponding closing parenthesis, and vice versa.

        Parameters
        ----------
        s : str
            The string of parentheses to check.

        Returns
        -------
        bool
            True if the string is valid, False otherwise.
        """
        if len(s) % 2 == 1:
            # If the length of the string is odd, it can't be valid.
            return False

        stack = []
        oppositeMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for char in s:
            if char in oppositeMap.values():
                # If the character is an open parenthesis, push it onto the stack.
                stack.append(char)
            elif len(stack) == 0:
                # If the character is a close parenthesis, but the stack is empty,
                # then the string is invalid.
                return False
            elif oppositeMap.get(char) == stack[len(stack) - 1]:
                # If the character is a close parenthesis, and the top of the stack
                # is the corresponding open parenthesis, then pop the top of the stack.
                stack.pop()
            else:
                # If the character is a close parenthesis, and the top of the stack
                # is not the corresponding open parenthesis, then the string is invalid.
                return False

        if len(stack) < 1:
            # If the stack is empty after iterating through the string, then the string is valid.
            return True
        # If the stack is not empty after iterating through the string, then the string is invalid.
        return False
                

import unittest

class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_single_open_parenthesis(self):
        self.assertFalse(self.solution.isValid("("))

    def test_single_close_parenthesis(self):
        self.assertFalse(self.solution.isValid(")"))

    def test_balanced_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("({[]})"))
        self.assertTrue(self.solution.isValid("((()))"))

    def test_unbalanced_parentheses(self):
        self.assertFalse(self.solution.isValid("(()"))
        self.assertFalse(self.solution.isValid(")()("))
        self.assertFalse(self.solution.isValid("({[}])"))

    def test_multiple_types_of_parentheses(self):
        self.assertTrue(self.solution.isValid("({[]})"))
        self.assertFalse(self.solution.isValid("({[})"))

    def test_long_string_with_balanced_parentheses(self):
        self.assertTrue(self.solution.isValid("((({[]}))())"))

    def test_long_string_with_unbalanced_parentheses(self):
        self.assertFalse(self.solution.isValid("((({[]}))())("))

if __name__ == '__main__':
    unittest.main()