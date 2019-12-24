class Solution:
    def canCross(self, stones) -> bool:
        if len(stones) == 0:
            return True
        if stones[1] > 1:
            return False
        ll = len(stones)
        j_val = {}
        for st in stones:
            j_val[st] = set()
        j_val[stones[1]].add(1)
        # print(j_val)
        for i in range(1, ll):
            for jump in j_val[stones[i]]:
                if jump > 0 and jump + stones[i] in j_val:
                    # if not j_val[jump + stones[i]].__contains__(jump):
                    j_val[jump + stones[i]].add(jump)
                # print('jump from', stones[i], 'to', jump + stones[i], jump)
                if jump - 1 > 0 and jump - 1 + stones[i] in j_val:
                    # if not j_val[jump - 1 + stones[i]].__contains__(jump - 1):
                    j_val[jump - 1 + stones[i]].add(jump - 1)
                # print('jump -1 from', stones[i], 'to', jump + stones[i], jump - 1)
                if jump + 1 + stones[i] in j_val:
                    # if not j_val[jump + 1 + stones[i]].__contains__(jump + 1):
                    j_val[jump + 1 + stones[i]].add(jump + 1)
                # print('jump +1 from', stones[i], 'to', jump + stones[i], jump + 1)
        # print(j_val)
        if j_val.get(stones[-1]):
            return True
        return False