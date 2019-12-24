class Solution:
    def minDeletionSize(self, A) -> int:
        def isSorted(A):
            return all(A[i] <= A[i + 1] for i in range(len(A) - 1))

        ans = 0
        raw = len(A)
        col = len(A[0])
        cur = ["" for i in range(raw)]
        for j in range(col):
            cur2 = cur[:]
            for i in range(raw):
                cur2[i] = cur2[i] + A[i][j]
            if isSorted(cur2):
                cur = cur2
            else:
                ans += 1
        return ans


if __name__ == "__main__":
    A = ["zyx", "wvu", "tsr"]
    sol = Solution()
    print(sol.minDeletionSize(A))
