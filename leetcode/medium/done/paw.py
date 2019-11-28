class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        ans = 1
        neg = 0
        if n < 0:
            neg = 1
            n = 0 - n
        while n:
            if n % 2:
                ans = ans * x
            n = n // 2
            x = x * x
        return ans * x
