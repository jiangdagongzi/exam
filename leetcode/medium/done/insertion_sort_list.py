# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        b = ListNode(0)
        t = b
        t.next = head
        head = head.next
        t.next.next = None
        while head:
            f = head.next
            head.next = None
            if t.next:
                if t.next.val > head.val:
                    c = t.next
                    t.next = head
                    head.next = c
                else:
                    t = t.next
                    head.next = f
                    continue
            else:
                t.next = head
            head = f
            t = b
        return b.next
