class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s) - 9):
            if s[i: i + 10] in d:
                d[s[i:i + 10]] = True
            else:
                d[s[i:i + 10]] = False
        return filter(lambda i: d[i], d)
