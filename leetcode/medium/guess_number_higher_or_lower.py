class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for len in range(2, n + 1):
            for start in range(1, n - len + 2):
                import sys
                res = sys.maxsize
                for k in range(start, len + start - 1):
                    ldp = dp[start][k - 1] if dp[start][k - 1] >= dp[k + 1][start + len - 1] else dp[k + 1][
                        start + len - 1]
                    res = res if res <= ldp + k else ldp + k
                dp[start][len + start - 1] = res
        # for dd in dp:
        #     print(dd)
        return dp[1][n]


if __name__ == "__main__":
    n = 5
    sol = Solution()
    print(sol.getMoneyAmount(n))
