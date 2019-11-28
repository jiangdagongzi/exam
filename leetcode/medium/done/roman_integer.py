class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''
        elif 1 <= num and num <= 3:
            return 'I' + self.intToRoman(num - 1)
        elif num == 4:
            return 'IV'
        elif 5 <= num and num <= 8:
            return 'V' + self.intToRoman(num - 5)
        elif num == 9:
            return 'IX'
        elif 10 <= num and num <= 39:
            return 'X' + self.intToRoman(num - 10)
        elif 40 <= num and num <= 49:
            return 'XL' + self.intToRoman(num - 40)
        elif 50 <= num and num <= 89:
            return 'L' + self.intToRoman(num - 50)
        elif 90 <= num and num <= 99:
            return 'XC' + self.intToRoman(num - 90)
        elif 100 <= num and num <= 399:
            return 'C' + self.intToRoman(num - 100)
        elif 400 <= num and num <= 499:
            return 'CD' + self.intToRoman(num - 400)
        elif 500 <= num and num <= 899:
            return 'D' + self.intToRoman(num - 500)
        elif 900 <= num and num <= 999:
            return 'CM' + self.intToRoman(num - 900)
        else:
            return 'M' + self.intToRoman(num - 1000)


if __name__ == '__main__':
    lst = 3
    sol = Solution()
    print(sol.intToRoman(lst))
