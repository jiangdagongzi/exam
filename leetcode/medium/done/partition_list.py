# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        temp = new_head
        if not temp.next or not temp.next.next:
            return head
        while temp.next:
            if temp.next.val < x:
                temp = temp.next
            else:
                break
        mid_tail = temp
        temp = temp.next
        while temp and temp.next:
            if temp.next.val < x:
                tar = temp.next
                temp.next = tar.next
                tar.next = mid_tail.next
                mid_tail.next = tar
                mid_tail = mid_tail.next
            else:
                temp = temp.next
        return new_head.next
