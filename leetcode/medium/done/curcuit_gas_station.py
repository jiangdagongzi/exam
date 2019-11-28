class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ll = len(gas)
        if ll == 1:
            if gas[0] - cost[0] < 0:
                return -1
            return 0
        val = []
        for i in range(ll):
            rest = gas[i] - cost[i]
            val.append(rest)
        for j in range(ll):
            rr = val[j]
            while rr >= 0:
                for k in range(j + 1, ll):
                    rr += val[k]
                    if rr < 0:
                        break
                if rr < 0:
                    break
                for p in range(j):
                    rr += val[p]
                    if rr < 0:
                        break
                if rr < 0:
                    continue
                return j
        return -1
