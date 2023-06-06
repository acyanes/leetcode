class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        seen = set()
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):
            if node not in seen:
                seen.add(node)
                for neigh in adj[node]:
                    if neigh != parent:
                        if neigh in seen:
                            return False
                        dfs(neigh, node)
                return True
        
        return dfs(0,-1) and len(seen)==n