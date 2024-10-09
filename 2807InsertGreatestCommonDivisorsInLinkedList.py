# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head):
        runner = head
        while runner.next != None:
            node = ListNode(self.gcd(runner.val, runner.next.val), runner.next)
            runner.next = node
            runner = runner.next.next

        return head