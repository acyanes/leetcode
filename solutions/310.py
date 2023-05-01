class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: 
            return [0]
        adj=defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        q = deque([])
        for k,v in adj.items():
            if len(v)==1:
                q.append(k)
        
        res=[]
        while n > 2:
            size = len(q)
            for _ in range(size):
                n -= 1
                removeNode = q.popleft()
                parent = adj[removeNode].pop()
                adj[parent].remove(removeNode)
                if len(adj[parent])==1:
                    q.append(parent)          
        return q