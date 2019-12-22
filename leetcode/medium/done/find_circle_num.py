class Solution:
    def findCircleNum(self, M) -> int:
        if not M:
            return 0
        n = len(M)

        def initG():
            graph = {}
            for i in range(n):
                graph[i] = []
            for i in range(n):
                for j in range(i + 1, n):
                    if M[i][j] == 1:
                        graph[i].append(j)
                        graph[j].append(i)
            return graph

        graph = initG()
        cls = [0 for i in range(n)]
        ll = [-1 for i in range(n)]
        for key in graph.keys():
            if cls[key] == 0:
                self.dfs(graph, cls, ll, key)
        ans = 0
        for p in ll:
            if p == -1:
                ans += 1
        return ans

    def dfs(self, graph, cls, ll, key):
        cls[key] = -1
        for val in graph[key]:
            if cls[val] == 0:
                ll[val] = key
                self.dfs(graph, cls, ll, val)
        cls[key] = 1


if __name__ == "__main__":
    M = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    sol = Solution()
    print(sol.findCircleNum(M))
