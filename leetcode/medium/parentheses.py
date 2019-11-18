class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if not n:
            return ans
        if n == 1:
            return ans.append('()')

    def insert(self, ans, pos):
        pass
