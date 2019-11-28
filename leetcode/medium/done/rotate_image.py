class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        c = 0
        n = len(matrix)
        i = 0
        while c <= n * n:
            for j in range(i, n - i - 1):
                print(matrix)
                temp1 = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                temp2 = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = temp1
                temp3 = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = temp2
                matrix[i][j] = temp3
                j += 1
                c += 4
            i += 1
            print(c)
            if n * n - c <= 1:
                break
        return matrix


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol = Solution()
    print(sol.rotate(matrix))
