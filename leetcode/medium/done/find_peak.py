class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        q = len(nums) - 1
        if q == 0:
            return 0
        while (q - p) > 1:
            half = (q + p) // 2
            if nums[half] < nums[half + 1]:
                p = half + 1
            else:
                q = half
        return p if nums[p] > nums[q] else q
