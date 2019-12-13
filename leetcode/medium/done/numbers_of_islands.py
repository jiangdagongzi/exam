class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        ll = len(grid)
        nn = len(grid[0])
        grid.insert(0, ["0" for i in range(nn + 2)])
        grid.append(["0" for i in range(nn + 2)])
        for i in range(1, ll + 1):
            grid[i].insert(0, "0")
            grid.append("0")
        ans = 0
        for i in range(1, ll + 1):
            for j in range(1, nn + 1):
                if grid[i][j] == "1":
                    lst = []
                    lst.append((i, j))
                    for nd in lst:
                        try:
                            if grid[nd[0]][nd[1] - 1] == "1":
                                lst.append((nd[0], nd[1] - 1))
                                grid[nd[0]][nd[1] - 1] = "0"
                            if grid[nd[0] - 1][nd[1]] == "1":
                                lst.append((nd[0] - 1, nd[1]))
                                grid[nd[0] - 1][nd[1]] = "0"
                            if grid[nd[0] + 1][nd[1]] == "1":
                                lst.append((nd[0] + 1, nd[1]))
                                grid[nd[0] + 1][nd[1]] = "0"
                            if grid[nd[0]][nd[1] + 1] == "1":
                                lst.append((nd[0], nd[1] + 1))
                                grid[nd[0]][nd[1] + 1] = "0"
                        except:
                            pass
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    sol = Solution()
    print(sol.numIslands(grid))
