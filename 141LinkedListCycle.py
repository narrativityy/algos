# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        """
        Checks if a linked list has a cycle in it.

        :param head: The head of the linked list.
        :type head: ListNode
        :return: True if the linked list has a cycle, False otherwise.
        :rtype: bool
        """
        seen = set()
        runner = head

        while runner:
            # If we have seen this node before, then there is a cycle in the list
            if runner in seen:
                return True
            seen.add(runner)
            runner = runner.next

        # If we have iterated over the whole list and haven't found a cycle, then there is no cycle
        return False

import unittest

class TestHasCycle(unittest.TestCase):
    def test_empty_linked_list(self):
        solution = Solution()
        self.assertFalse(solution.hasCycle(None))

    def test_linked_list_with_no_cycle(self):
        solution = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        self.assertFalse(solution.hasCycle(node1))

    def test_linked_list_with_cycle(self):
        solution = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1
        self.assertTrue(solution.hasCycle(node1))

    def test_linked_list_with_single_node_and_cycle(self):
        solution = Solution()
        node1 = ListNode(1)
        node1.next = node1
        self.assertTrue(solution.hasCycle(node1))

    def test_linked_list_with_multiple_nodes_and_cycle(self):
        solution = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        self.assertTrue(solution.hasCycle(node1))

if __name__ == '__main__':
    unittest.main()