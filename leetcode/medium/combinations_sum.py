class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dict = {}
        for i in range(target):
            dict[i] = []
        for i in range(1, target + 1):
            for j in candidates:
                if i == j:
                    dict[i].append([i])
                elif i > j:
                    for k in dict[i - j]:
                        x = k[:]
                        x.append(j)
                        x.sort()
                        if x not in dict[i]:
                            dict[i].append(x)
        return dict[target]
