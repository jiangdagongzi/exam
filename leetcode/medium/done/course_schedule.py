# time = 0
#
#
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites) -> bool:
#         vl = []
#         for i in range(numCourses):
#             vt = vertex(i)
#             vt.color = 0
#             vl.append(vt)
#         for eg in prerequisites:
#             vl[eg[1]].adj.append(vl[eg[0]])
#         bl = []
#         for u in vl:
#             if u.color == 0:
#                 bl.append(self.dfs(vl, u))
#         for u in vl:
#             print(u.color, u.p, u.d, u.f, u.v)
#
#     def dfs(self, vl, u):
#         global time
#         time += 1
#         u.d = time
#         u.color = 1
#         for v in u.adj:
#             if v.color == 0:
#                 v.p = u
#                 self.dfs(vl, v)
#         u.color = 2
#         time += 1
#         u.f = time
#         return True
#
#
# class vertex(object):
#     def __init__(self, v):
#         self.color = None
#         self.p = None
#         self.d = None
#         self.v = v
#         self.f = None
#         self.adj = []
#
#
# if __name__ == '__main__':
#     numCourses = 2
#     prerequisites = [[1, 0], [0, 1]]
#     sol = Solution()
#     print(sol.canFinish(numCourses, prerequisites))
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        def dfs(i, adj, flags):
            if flags[i] == -1:
                return False
            if flags[i] == 1:
                return True
            flags[i] = -1
            for j in adj[i]:
                if not dfs(j, adj, flags):
                    return False
            flags[i] = 1
            return True

        adj = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adj, flags):
                return False
        return True