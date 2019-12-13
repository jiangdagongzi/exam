class Solution:
    def sort(self, x, y):
        ll = x + y
        rr = y + x
        return 1 if ll > rr else 0

    def largestNumber(self, nums) -> str:
        if not nums:
            return ""
        if sum(nums) == 0:
            return "0"
        slst = [str(n) for n in nums]
        slst.sort(self.sort, reverse=True)
        return ''.join(slst)
