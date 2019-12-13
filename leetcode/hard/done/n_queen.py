class Solution:
    def solveNQueens(self, n: int):
        pz = [["." for i in range(n)] for j in range(n)]
        lst = []
        ans = []
        sp_next = self.ck(pz, 0)
        qz = pz.copy()
        for sp in sp_next:
            lst.append((0, sp, self.put(qz, (0, sp))))
        for (i, j, qz) in lst:
            if i == n:
                continue
            # print("based on ", i, j)
            # for oo in qz:
            #     print(oo)
            sp_next = self.ck(qz, i + 1)
            for sp in sp_next:
                lst.append((i + 1, j, self.put(qz, (i + 1, sp))))
        for (i, _, qz) in lst:
            if i == n - 1:
                qqqqq = []
                for a in range(len(qz)):
                    aa = ""
                    for b in range(len(qz[a])):
                        if qz[a][b] != "Q":
                            aa += "."
                        else:
                            aa += "Q"
                    qqqqq.append(aa)
                ans.append(qqqqq)
        return ans

    def put(self, qz, q):
        ll = len(qz)
        pz = [[str(qz[j][i]) for i in range(ll)] for j in range(ll)]
        x, y = q
        pz[x][y] = "Q"
        for i in range(ll):
            if i != x:
                pz[i][y] += "*"
            if i != y:
                pz[x][i] += "*"
        i = x
        j = y
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            pz[i][j] += "*"
        i = x
        j = y
        while i < ll - 1 and j > 0:
            i += 1
            j -= 1
            pz[i][j] += "*"
        i = x
        j = y
        while i > 0 and j < ll - 1:
            i -= 1
            j += 1
            pz[i][j] += "*"
        i = x
        j = y
        while i < ll - 1 and j < ll - 1:
            i += 1
            j += 1
            pz[i][j] += "*"
        # print("base ")
        # for oo in qz:
        #     print(oo)
        # print("added ", x, y)
        # for oo in pz:
        #     print(oo)
        return pz

    def ck(self, pz, i):
        ll = []
        if i == len(pz):
            return []
        for j in range(len(pz[0])):
            if pz[i][j] == ".":
                ll.append(j)
        return ll


if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.solveNQueens(4))
