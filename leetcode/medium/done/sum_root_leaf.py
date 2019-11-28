# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        lst.append((root, root.val))
        sum = 0
        for node, prc in lst:
            if node.left == None and node.right == None:
                sum += node.val
            if node.left:
                lst.append((node.left, 10 * prc + node.left.val))
            if node.right:
                lst.append((node.right, 10 * prc + node.right.val))
        return sum
