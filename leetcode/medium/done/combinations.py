class combinations(object):
    def combine(self, n, k):
        """
        :param n: int
        :param k: int
        :return: List[List[int]]
        """
        if k == 0 or k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        lst = self.combine(n - 1, k)
        for item in self.combine(n-1, k-1):
            item.append(n)
            lst.append(item)
        return lst
