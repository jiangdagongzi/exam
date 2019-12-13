# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return
        lst = []
        lst.append((root, root.val, [root.val]))
        ans = []
        for nd, sm, pt in lst:
            if nd.left:
                cp = pt.copy()
                cp.append(nd.left.val)
                lst.append((nd.left, sm + nd.left.val, cp))
            if nd.right:
                cp = pt.copy()
                cp.append(nd.right.val)
                lst.append((nd.right, sm + nd.right.val, cp))
            if not nd.left and not nd.right and sm == sum:
                ans.append(pt)
        return ans
