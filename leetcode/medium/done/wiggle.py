class Solution:
    def wiggleMaxLength(self, nums) -> int:
        nn = len(nums)
        if nn <= 1:
            return nn
        i = 1
        while i < len(nums) - 1:
            if (nums[i] - nums[i - 1]) * (nums[i + 1] - nums[i]) >= 0:
                print(nums.pop(i), 'eeee')
                i -= 1
            i += 1
        print(nums)
        if len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2
        return len(nums)


if __name__ == "__main__":
    nums = [0, 0, 0]
    sol = Solution()
    print(sol.wiggleMaxLength(nums))
