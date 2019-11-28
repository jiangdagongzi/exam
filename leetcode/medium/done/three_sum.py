class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        ll = len(nums)
        kk = 0
        while kk < ll - 2:
            ii = kk + 1

            jj = ll - 1
            while ii < jj:
                if nums[ii] + nums[jj] + nums[kk] == 0:
                    lst = []
                    lst.append(nums[ii])
                    lst.append(nums[jj])
                    lst.append(nums[kk])
                    ans.append(lst)
                    while nums[ii] + nums[jj] + nums[kk] == 0:
                        ii += 1
                        if ii == jj:
                            break
                elif nums[ii] + nums[jj] + nums[kk] < 0:
                    ii += 1
                    continue
                else:
                    jj -= 1
                    continue
            kk += 1
            while nums[kk] == nums[kk-1] and kk < ii:
                kk +=1
        return ans
