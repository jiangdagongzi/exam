class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while c<=n*n:
            for i in range(j, n-j):
                array[j][i] = c
                c += 1
            for i in range(j+1, n-j):
                array[i][n-j-1] = c
                c += 1
            for i in range(n-j-2, j-1, -1):
                array[n-j-1][i] = c
                c += 1
            for i in range(n-j-2, j, -1):
                array[i][j] = c
                c += 1
            j += 1
        return array