class Solution:
    def maxWidthRamp(self, nums) -> int:
        if not nums:
            return 0
        ll = len(nums)
        nn = []
        nn.append(0)
        res = 0
        for i in range(ll):
            if nums[nn[-1]] > nums[i]:
                nn.append(i)
        for i in range(ll):
            rr = ll - i - 1
            while nums[nn[-1]] <= nums[rr]:
                res = res if res > rr - nn[-1] else rr - nn[-1]
                nn.pop(-1)
                if not nn:
                    return res
        return res


if __name__ == "__main__":
    nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    sol = Solution()
    print(sol.maxWidthRamp(nums))
