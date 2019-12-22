# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(nd):
            if not nd: return None
            if nd in dic:
                return dic[nd]
            clone = Node(nd.val, [])
            dic[nd] = clone
            for i in nd.neighbors:
                clone.neighbors.append(dfs(i))
            return clone

        dic = {}
        return dfs(node)
