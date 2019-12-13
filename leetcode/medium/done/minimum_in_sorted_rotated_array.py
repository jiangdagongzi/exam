class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return
        p = 0
        q = len(nums) - 1
        if nums[q] > nums[p]:
            return nums[p]
        while p < q - 1:
            mid = (p + q) // 2
            if nums[p] > nums[mid]:
                q = mid
            else:
                p = mid
        return nums[p] if nums[p] < nums[q] else nums[q]
