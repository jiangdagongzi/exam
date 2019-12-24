class Solution:
    def numEnclaves(self, A) -> int:
        def dfs(i, j, A, tms, flg):
            if cls[i - 1][j - 1] != -1:
                return tms, flg
            cls[i - 1][j - 1] = 0
            if i == 1 or j == 1 or i == raw or j == col:
                flg = 0
            tms += 1
            for ee in adj[i - 1][j - 1]:
                x, y = ee
                tms, flg = dfs(x, y, A, tms, flg)
            return tms, flg

        if not A:
            return 0
        raw = len(A)
        col = len(A[0])
        adj = [[[] for i in range(col)] for j in range(raw)]
        cls = [[-1 for i in range(col)] for j in range(raw)]
        for i in range(raw):
            A[i].insert(0, 0)
            A[i].append(0)
        sm = 0
        A.insert(0, [0 for i in range(col + 2)])
        A.append([0 for i in range(col + 2)])

        for i in range(0, raw + 2):
            for j in range(0, col + 2):
                if A[i][j] == 1:
                    if A[i - 1][j] == 1:
                        adj[i - 1][j - 1].append((i - 1, j))
                    if A[i][j - 1] == 1:
                        adj[i - 1][j - 1].append((i, j - 1))
                    if A[i + 1][j] == 1:
                        adj[i - 1][j - 1].append((i + 1, j))
                    if A[i][j + 1] == 1:
                        adj[i - 1][j - 1].append((i, j + 1))
        for i in range(1, raw + 1):
            for j in range(1, col + 1):
                if A[i][j] == 1:
                    tms = 0
                    flg = 1
                    tms, flg = dfs(i, j, A, tms, flg)
                    cls[i - 1][j - 1] = 1
                    sm += tms * flg
                # print("kkkkkkkkkkk")
        return sm


if __name__ == "__main__":
    A = [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
         [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
         [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]
    sol = Solution()
    print(sol.numEnclaves(A))
