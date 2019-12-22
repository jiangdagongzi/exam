class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(num1, num2, s):
            if num1.startswith("0") and len(num1) > 1:
                return False
            if num2.startswith("0") and len(num2) > 1:
                return False
            tmp = str(int(num1) + int(num2))
            lt = len(tmp)
            if s.startswith(tmp):
                num1, num2 = num2, tmp
                s = s[lt:]
                if s == "":
                    return True
                return isValid(num1, num2, s)
            return False

        n = len(num)
        for i in range(1, (n + 1) // 2):
            num1 = num[0:i]
            for j in range(i + 1, n):
                num2 = num[i:j]
                if isValid(num1, num2, num[j:]):
                    return True
        return False


if __name__ == "__main__":
    nums = "0235813"
    sol = Solution()
    print(sol.isAdditiveNumber(nums))
