class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m ==1 or n == 1:
            return 1
        count = [[0] * n for x in range(m)]
        for i in range(1, n):
            count[0][i] = 1
        for j in range(1, m):
            count[j][0] = 1
        for a in range(1, m):
            for b in range(1, n):
                count[a][b] = count[a - 1][b] + count[a][b - 1]
        return count[m - 1][n - 1]
