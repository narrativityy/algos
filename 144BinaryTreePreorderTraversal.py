# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        """
        Returns the preorder traversal of a binary tree as a list of node values.

        :param root: The root of the binary tree.
        :type root: TreeNode
        :return: A list of node values representing the preorder traversal of the binary tree.
        :rtype: List[int]
        """
        # Head is used to keep track of the current node
        head = root
        
        # Stack is used to store the right children of the nodes
        stack = []
        
        # Res is used to store the result
        res = []
        
        # Traverse the binary tree
        while head or stack:
            # If the head is not None
            if head:
                # Add the value of the current node to the result
                res.append(head.val)
                
                # If the right child of the current node is not None
                if head.right:
                    # Add it to the stack
                    stack.append(head.right)
                
                # Move to the left child of the current node
                head = head.left
            else:
                # If the head is None, pop the last node from the stack and move to it
                head = stack.pop()
        
        # Return the result
        return res
        
        

        
import unittest

class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.preorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.preorderTraversal(root), [1])

    def test_two_nodes_left_child(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2])

    def test_two_nodes_right_child(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2])

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 4, 5, 3, 6, 7])

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()