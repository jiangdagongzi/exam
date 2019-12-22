class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return 0
        ll = len(nums)
        left_pro = []
        left_pro.append(nums[0])
        for i in range(1, ll):
            left_pro.append(nums[i] * left_pro[i - 1])
        print(left_pro)
        right_pro = []
        right_pro.append(nums[ll - 1])
        for i in range(1, ll):
            right_pro.insert(0, right_pro[0] * nums[ll - 1 - i])
        print(right_pro)
        output = []
        output.append(right_pro[1])
        for i in range(1, ll - 1):
            output.append(left_pro[i - 1] * right_pro[i + 1])
        output.append(left_pro[ll - 2])
        return output


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 1, 2]
    print(sol.productExceptSelf(nums))
