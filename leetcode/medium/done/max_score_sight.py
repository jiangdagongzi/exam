class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        ans = 0
        pre = A[0]
        for j in range(1, len(A)):
            ans = ans if ans > pre + A[j] - j else pre + A[j] - j
            pre = pre if pre > A[j] + j else A[j] + j
        return ans


if __name__ == "__main__":
    nums = [8, 1, 5, 2, 6]
    sol = Solution()
    print(sol.maxScoreSightseeingPair(nums))
