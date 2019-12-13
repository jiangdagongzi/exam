class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
                continue
            if nums[j] == 0:
                nums.pop(j)
                nums.insert(0, 0)
                i += 1
                continue
            if nums[i] == 1:
                i += 1
            if nums[j] == 2:
                j -= 1
            if nums[i] == 2:
                while nums[j] != 1:
                    if nums[j] == 0:
                        nums.pop(j)
                        nums.insert(0, 0)
                        i += 1
                        continue
                    else:
                        j -= 1
                nums[i] = 1
                nums[j] = 2
                i += 1
                j -= 1

        if nums[i] == 0:
            nums.pop(i)
            nums.insert(0, 0)
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    print(sol.sortColors(nums))
