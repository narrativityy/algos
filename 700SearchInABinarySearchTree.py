class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    """
    Searches the binary search tree for a given value and returns the node if found.
    
    Args:
        root (TreeNode): The root of the binary search tree.
        val (int): The value to search for.
        
    Returns:
        TreeNode: The node with the given value if found, None otherwise.
    """
    current = root

    while current != None and current.val != val:
        # If the current node's value is greater than the value we are looking for,
        # then the value must be in the left subtree.
        if current.val > val:
            current = current.left
        # Otherwise, the value must be in the right subtree.
        else:
            current = current.right
    
    # Return the node with the given value if found, None otherwise.
    return current

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSearchBST(unittest.TestCase):
    def test_search_existing_value(self):
        # Create a tree with nodes 4, 2, 7, 1, 3
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        self.assertEqual(searchBST(root, 2).val, 2)
        self.assertEqual(searchBST(root, 7).val, 7)
        self.assertEqual(searchBST(root, 1).val, 1)
        self.assertEqual(searchBST(root, 3).val, 3)

    def test_search_non_existing_value(self):
        # Create a tree with nodes 4, 2, 7, 1, 3
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        self.assertIsNone(searchBST(root, 5))

    def test_search_empty_tree(self):
        self.assertIsNone(searchBST(None, 5))

    def test_search_tree_with_one_node(self):
        root = TreeNode(5)
        self.assertEqual(searchBST(root, 5).val, 5)
        self.assertIsNone(searchBST(root, 3))

    def test_search_tree_with_multiple_nodes(self):
        # Create a tree with nodes 4, 2, 7, 1, 3, 6, 8
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)

        self.assertEqual(searchBST(root, 2).val, 2)
        self.assertEqual(searchBST(root, 7).val, 7)
        self.assertEqual(searchBST(root, 1).val, 1)
        self.assertEqual(searchBST(root, 3).val, 3)
        self.assertEqual(searchBST(root, 6).val, 6)
        self.assertEqual(searchBST(root, 8).val, 8)

if __name__ == '__main__':
    unittest.main()