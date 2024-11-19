class MinStack:

    """
    MinStack is a stack that also keeps track of the minimum value currently in the stack.

    Attributes:
        stack (list): The list of values in the stack.
        minStack (list): The list of minimum values in the stack.
    """

    def __init__(self):
        """
        Initializes the stack and the minStack.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack and updates the minStack.

        Args:
            val: The value to push onto the stack.
        """
        self.stack.append(val)

        # If the minStack is empty, push the value onto the minStack
        if len(self.minStack) == 0:
            self.minStack.append(val)
        # If the value is less than the current minimum, push the value onto the minStack
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            # Otherwise, push the current minimum onto the minStack again
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        """
        Removes the top element from the stack and updates the minStack.
        
        Returns:
            None
        """
        # Remove the top element from the minStack
        self.minStack.pop()
        # Remove and return the top element from the stack
        return self.stack.pop()

    def top(self) -> int:
        """
        Returns the top element from the stack without removing it.

        Returns:
            int: The top element from the stack.
        """
        # Return the top element from the stack
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.

        Returns:
            int: The minimum element in the stack.
        """
        # Return the top element from the minStack, which is the current minimum
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

import unittest

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def test_initialization(self):
        self.assertEqual(self.min_stack.stack, [])
        self.assertEqual(self.min_stack.minStack, [])

    def test_push_single_element(self):
        self.min_stack.push(5)
        self.assertEqual(self.min_stack.stack, [5])
        self.assertEqual(self.min_stack.minStack, [5])

    def test_push_multiple_elements(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.assertEqual(self.min_stack.stack, [5, 3, 7])
        self.assertEqual(self.min_stack.minStack, [5, 3, 3])

    def test_getMin_after_push(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.assertEqual(self.min_stack.getMin(), 3)

    def test_pop_after_push(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.stack, [5, 3])
        self.assertEqual(self.min_stack.minStack, [5, 3])

    def test_getMin_after_pop(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 3)

    def test_top_after_push(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.assertEqual(self.min_stack.top(), 7)

    def test_top_after_pop(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.push(7)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 3)

if __name__ == '__main__':
    unittest.main()