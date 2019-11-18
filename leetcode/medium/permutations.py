class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            ll = []
            ll.append(nums)
            return ll
        else:
            per = []
            curr = self.permute(nums[:-1])
            for lst in curr:
                for i in range(len(lst) + 1):
                    curr1 = lst.copy()
                    curr1.insert(i, nums[-1])
                    per.append(curr1)
            return per


if __name__ == '__main__':
    lst = [1, 2, 3]
    sol = Solution()
    print(sol.permute(lst))
