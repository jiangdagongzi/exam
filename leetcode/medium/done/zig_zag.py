class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ii = 0
        matrix = []
        for i in range(numRows):
            lst = []
            matrix.append(lst)
        towards = 0
        if_first = 0
        while ii < len(s):
            for j in range(numRows - if_first):
                if not towards:
                    matrix[j + if_first].append(s.__getitem__(ii))
                else:
                    matrix[numRows - j - 1 - if_first].append(s.__getitem__(ii))
                ii += 1
                if ii == len(s):
                    break
            towards = 0 if towards == 1 else 1
            if_first = 1
        st = str('')
        for ll in matrix:
            for ss in ll:
                st = st + ss
        return st


if __name__ == '__main__':
    sol = Solution()
    ss = "AB"
    n = 1
    print('sadasf', sol.convert(ss, n))
