class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k == 1:
            return nums
        if k % 2 == 1:
            odd = True
        else:
            odd = False
        if k == len(nums):
            nums.sort()
            ans = []
            ans.append(nums[k // 2] if odd else (nums[k // 2] + nums[k // 2 + 1]) / 2)
            return ans
        cur = nums[0:k].copy()
        cur.sort()
        ans = []
        ans.append(cur[k // 2] if odd else (cur[k // 2] + cur[k // 2 + 1]) / 2)
        for i in range(k, len(nums)):
            rem = i - k
            p = 0
            q = k - 1
            print(cur)
            while q - p > 1:
                mid = (p + q) // 2
                if cur[mid] < nums[rem]:
                    p = mid
                else:
                    q = mid
            if cur[p] == nums[rem]:
                cur.pop(p)
            else:
                cur.pop(q)
            print(p, q, "lll", cur)
            p = 0
            q = k - 2
            while q - p > 1:
                mid = (p + q) // 2
                if cur[mid] < nums[i]:
                    p = mid
                else:
                    q = mid
            if cur[q] < nums[i]:
                cur.insert(q + 1, nums[i])
            elif cur[p] > nums[i]:
                cur.insert(p, nums[i])
            else:
                cur.insert(p + 1, nums[i])
            print(p, q, "lll", cur)
            ans.append(cur[k // 2] if odd else (cur[k // 2] + cur[k // 2 + 1]) / 2)
        return ans
