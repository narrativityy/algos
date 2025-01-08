# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists into one sorted linked list.

        :param list1: The first sorted linked list.
        :type list1: ListNode
        :param list2: The second sorted linked list.
        :type list2: ListNode
        :return: The head of the merged sorted linked list.
        :rtype: ListNode
        """
        # Initialize a dummy node to act as the starting point for the merged list
        head = runner = ListNode()

        # Traverse both lists until we reach the end of one
        while list1 and list2:
            # Compare the current nodes of both lists and attach the smaller one to the merged list
            if list1.val < list2.val:
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next
            # Move the runner to the next node in the merged list
            runner = runner.next
        
        # At the end of the loop, attach the remaining elements of the non-empty list
        runner.next = list1 or list2

        # Return the merged list, starting from the next node of the dummy
        return head.next

import unittest

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_two_empty_lists(self):
        list1 = None
        list2 = None
        self.assertIsNone(self.solution.mergeTwoLists(list1, list2))

    def test_merge_one_empty_list_and_one_non_empty_list(self):
        list1 = ListNode(1)
        list2 = None
        merged_list = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(merged_list.val, 1)
        self.assertIsNone(merged_list.next)

    def test_merge_two_non_empty_lists_with_same_length(self):
        list1 = ListNode(1)
        list1.next = ListNode(3)
        list2 = ListNode(2)
        list2.next = ListNode(4)
        merged_list = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(merged_list.val, 1)
        self.assertEqual(merged_list.next.val, 2)
        self.assertEqual(merged_list.next.next.val, 3)
        self.assertEqual(merged_list.next.next.next.val, 4)
        self.assertIsNone(merged_list.next.next.next.next)

    def test_merge_two_non_empty_lists_with_different_lengths(self):
        list1 = ListNode(1)
        list1.next = ListNode(3)
        list2 = ListNode(2)
        list2.next = ListNode(4)
        list2.next.next = ListNode(5)
        merged_list = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(merged_list.val, 1)
        self.assertEqual(merged_list.next.val, 2)
        self.assertEqual(merged_list.next.next.val, 3)
        self.assertEqual(merged_list.next.next.next.val, 4)
        self.assertEqual(merged_list.next.next.next.next.val, 5)
        self.assertIsNone(merged_list.next.next.next.next.next)

    def test_merge_two_non_empty_lists_with_duplicate_values(self):
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list2 = ListNode(1)
        list2.next = ListNode(3)
        merged_list = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(merged_list.val, 1)
        self.assertEqual(merged_list.next.val, 1)
        self.assertEqual(merged_list.next.next.val, 2)
        self.assertEqual(merged_list.next.next.next.val, 3)
        self.assertIsNone(merged_list.next.next.next.next)

if __name__ == '__main__':
    unittest.main()