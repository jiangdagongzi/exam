class Solution:
    def maxCoins(self, nums) -> int:
        nums.insert(0, 1)
        nums.append(1)
        ll = len(nums)
        dp = [[0 for j in range(ll)] for i in range(ll)]
        dp[0][0] = dp[ll - 1][ll - 1] = 1
        for i in range(1, ll - 1):
            dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]
        for l in range(2, ll - 1):
            for i in range(1, ll - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    left = 0 if k == i else dp[i][k - 1]
                    right = 0 if k == j else dp[k + 1][j]
                    dp[i][j] = dp[i][j] if dp[i][j] > (left + right + nums[i-1] * nums[k] * nums[j+1]) else (
                            left + right + nums[i-1] * nums[k] * nums[j+1])

        return dp[1][ll - 2]


if __name__ == '__main__':
    dp = [[0 for j in range(10)] for i in range(10)]
    print(dp)
