class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        sum = [[0] * m for x in range(n)]
        # print(sum)
        sum[0][0] = grid[0][0]
        for i in range(1, m):
            sum[0][i] = grid[0][i] + sum[0][i - 1]
        for j in range(1, n):
            sum[j][0] = grid[j][0] + sum[j - 1][0]
        for ii in range(1, n):
            for jj in range(1, m):
                last = sum[ii - 1][jj] if sum[ii - 1][jj] < sum[ii][jj - 1] else sum[ii][jj- 1]
                sum[ii][jj] = grid[ii][jj] + last
        return sum[n-1][m-1]


# val, x, y, next, sum
#         temp = Node(grid[0][0], 0, 0, grid[0][0])
#         lst = []
#         lst.append(temp)
#         n = len(grid)
#         m = len(grid[0])
#         des = []
#         for item in lst:
#             item.show()
#             if item.x == n - 1 and item.y == m - 1:
#                 des.append(item)
#                 continue
#             try:
#                 ii = Node(grid[item.x][item.y + 1], item.x, item.y + 1, item.sum + grid[item.x][item.y + 1])
#                 lst.append(ii)
#             except:
#                 pass
#             try:
#                 jj = Node(grid[item.x + 1][item.y], item.x + 1, item.y, item.sum + grid[item.x + 1][item.y])
#                 lst.append(jj)
#             except:
#                 pass
#         min = des[0].sum
#         for iter in des:
#             print(iter.sum, min)
#             if iter.sum < min:
#                 min = iter.sum
#         return min
#
#
# class Node(object):
#     def __init__(self, val, x, y, sum):
#         self.val = val
#         self.x = x
#         self.y = y
#         self.sum = sum
#
#     def show(self):
#         print(self.val, self.x, self.y, self.sum)


if __name__ == '__main__':
    sol = Solution()
    grid = [[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
            [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
            [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
            [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
            [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
            [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
            [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
            [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
            [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
            [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
            [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
            [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
    print(sol.minPathSum(grid))
