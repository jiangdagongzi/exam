# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return
        if m == n:
            return head
        bh = ListNode(0)
        bh.next = head
        pos = 0
        t = bh
        lst = []
        while pos < m - 1:
            t = t.next
            pos += 1
        q = t
        t = t.next
        pos += 1
        while pos <= n:
            lst.append(t)
            t = t.next
            pos += 1
        while lst:
            q.next = lst.pop()
            q = q.next
        q.next = t
        return bh.next
