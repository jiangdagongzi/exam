class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ss = 1
        for i in range(1, n):
            ss *= i
            if ss > k:
                return self.getPermutation(i, k)
