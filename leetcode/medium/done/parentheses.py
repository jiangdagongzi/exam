class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return
        ans = []
        if n == 1:
            ans.append('()')
            return ans
        h = 2 * n
        root = Node('(', 1, 0)
        lst = []
        lst.append(root)
        ans = []
        for node in lst:
            if node.left_num + node.right_num == h:
                ans.append(node.val)
            if node.left_num < n:
                node.left = Node(node.val + '(', node.left_num + 1, node.right_num)
                lst.append(node.left)
            if node.right_num < node.left_num:
                node.right = Node(node.val + ')', node.left_num , node.right_num+1)
                lst.append(node.right)
        return ans


class Node:
    def __init__(self, val, left_num, right_num):
        self.val = val
        self.left = None
        self.right = None
        self.left_num = left_num
        self.right_num = right_num
