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


