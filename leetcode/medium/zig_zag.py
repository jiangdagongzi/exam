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
            # print('i', ii, s.__getitem__(ii))
            for j in range(numRows - if_first):
                if not towards:
                    matrix[j + if_first].append(s.__getitem__(ii))
                    print('i', ii)
                    print('j', j + if_first, matrix[j + if_first])
                else:
                    matrix[numRows - j - 1 - if_first].append(s.__getitem__(ii))
                    print('numRows - j - 1', numRows - j - 1 - if_first, matrix[numRows - j - 1 - if_first])
                ii += 1
                print('i', ii)
                if ii == len(s):
                    print('break')
                    break
                # print('ii++')
            towards = 0 if towards == 1 else 1
            if_first = 1
        st = str('')
        for ll in matrix:
            for ss in ll:
                # print('ll', ll)
                # print('ss', ss)
                st = st + ss
                # print(st)
            print('st', st)
        return st


if __name__ == '__main__':
    sol = Solution()
    ss = "AB"
    n = 1
    print('sadasf', sol.convert(ss, n))
