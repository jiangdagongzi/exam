# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        aa = []
        lst = []
        lst.append(root)
        aa.append(lst)
        for cur in aa:
            ll = []
            for nd in cur:
                if nd.left:
                    ll.append(nd.left)
                if nd.right:
                    ll.append(nd.right)
            if ll:
                aa.append(ll)
        ans = []
        for ss in aa:
            nn = map(lambda i: i.val, ss)
            ans.append(nn)
        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.left = TreeNode(7)
    sol = Solution()
    sol.levelOrder(root)