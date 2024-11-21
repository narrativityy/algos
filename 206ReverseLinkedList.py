# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        """
        Reverses a singly linked list.

        :param head: The head of the list to reverse.
        :type head: ListNode
        :return: The new head of the reversed list.
        :rtype: ListNode
        """
        if not head:
            return None

        # If the list is empty, return None.

        newHead = head
        if head.next:
            # If the list has more than one element, recursively call reverseList on the next element.
            newHead = self.reverseList(head.next)
            # Then, set the next of the current head to the previous head.
            head.next.next = head
        # Set the next of the current head to None.
        head.next = None
        
        return newHead

import unittest

class TestReverseList(unittest.TestCase):
    def test_empty_list(self):
        solution = Solution()
        self.assertIsNone(solution.reverseList(None))

    def test_single_node(self):
        solution = Solution()
        node = ListNode(1)
        reversed_node = solution.reverseList(node)
        self.assertEqual(reversed_node.val, 1)
        self.assertIsNone(reversed_node.next)

    def test_multiple_nodes(self):
        solution = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        reversed_node = solution.reverseList(node1)
        self.assertEqual(reversed_node.val, 3)
        self.assertEqual(reversed_node.next.val, 2)
        self.assertEqual(reversed_node.next.next.val, 1)
        self.assertIsNone(reversed_node.next.next.next)

    def test_two_nodes(self):
        solution = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        reversed_node = solution.reverseList(node1)
        self.assertEqual(reversed_node.val, 2)
        self.assertEqual(reversed_node.next.val, 1)
        self.assertIsNone(reversed_node.next.next)

if __name__ == '__main__':
    unittest.main()