# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        """
        Returns the postorder traversal of a binary tree as a list of node values.

        :param root: The root of the binary tree.
        :type root: TreeNode
        :return: A list of node values representing the postorder traversal of the binary tree.
        :rtype: List[int]
        """
        arr = []
        def postorder(root):
            """
            A recursive helper function to perform the postorder traversal of the binary tree.
            """
            if root:
                # Traverse the left subtree
                postorder(root.left)
                # Traverse the right subtree
                postorder(root.right)
                # Append the current node's value to the result list
                arr.append(root.val)
        
        # Start the postorder traversal from the root
        postorder(root)
        return arr

import unittest

class TestPostorderTraversal(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        root = None
        result = solution.postorderTraversal(root)
        self.assertEqual(result, [])

    def test_single_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        result = solution.postorderTraversal(root)
        self.assertEqual(result, [1])

    def test_binary_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        result = solution.postorderTraversal(root)
        self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

if __name__ == '__main__':
    unittest.main()