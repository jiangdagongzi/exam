class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(nums)
        if not nums:
            return [[]]
        if len(nums) == 1:
            ans = []
            sub1 = []
            sub2 = []
            sub2.append(nums[0])
            ans.append(sub1)
            ans.append(sub2)
            print('ans', ans)
            return ans
        temp = self.subsets(nums[:-1])
        temp2 = []
        for lst in temp:
            ll = lst.copy()
            ll.append(nums[-1])
            temp2.append(ll)
        temp.extend(temp2)
        return temp


if __name__ == '__main__':
    sol = Solution()
    lst = [1, 2, 3]
    print(sol.subsets(lst))
