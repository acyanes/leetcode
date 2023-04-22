class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = [] 

        def dfs(node, path):
            if node == n-1:
                res.append(path[:])
                return

            for neigh in graph[node]:
                path.append(neigh)
                dfs(neigh, path)
                path.pop()
        dfs(0, [0])
        return res