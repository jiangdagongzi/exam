# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        ans = curr
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = carry + val1 + val2
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return ans.next
