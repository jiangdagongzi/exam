class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        same = 0
        count = 1
        for i in range(len(nums) - 1):
            print(nums[i], nums[i + 1], nums[i] & nums[i + 1])

            if nums[i] & nums[i + 1] == nums[i]:
                if same:
                    nums.pop(i + 1)
                    i -= 1
                    print('nums', nums)
                else:
                    count += 1
            else:
                same = 0
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    lst = [1, 1, 1, 2, 2, 3]
    print(sol.removeDuplicates(lst))
