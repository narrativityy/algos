class Solution:
    def evalRPN(self, tokens) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        :param tokens: The list of tokens in Reverse Polish Notation.
        :type tokens: List[str]
        :return: The value of the evaluated expression.
        :rtype: int
        """
        stack = []

        for token in tokens:
            if self.is_number(token):
                stack.append(token)
            else:
                if token == '+':
                    # Pop two numbers from the stack and add them
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif token == '-':
                    # Pop two numbers from the stack and subtract the second from the first
                    firstNum = int(stack.pop())
                    secondNum = int(stack.pop())
                    stack.append(secondNum - firstNum)
                elif token == '*':
                    # Pop two numbers from the stack and multiply them
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif token == '/':
                    # Pop two numbers from the stack and divide the second by the first
                    firstNum = int(stack.pop())
                    secondNum = int(stack.pop())
                    stack.append(secondNum / firstNum)
            
        return int(stack[0])


    def is_number(self, s):
        """
        Checks if the given string is a number.

        :param s: The string to check.
        :type s: str
        :return: True if the string is a number, False otherwise.
        :rtype: bool
        """
        try:
            # Attempt to convert the string to a float
            float(s)
            return True
        except ValueError:
            # If the conversion fails, the string is not a number
            return False

import unittest

class TestEvalRPN(unittest.TestCase):
    def test_single_number(self):
        tokens = ["2"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 2)

    def test_addition(self):
        tokens = ["2", "3", "+"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        tokens = ["5", "2", "-"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        tokens = ["3", "4", "*"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 12)

    def test_division(self):
        tokens = ["10", "2", "/"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 5)

    def test_complex_expression(self):
        tokens = ["2", "1", "+", "3", "*", "4", "-"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()