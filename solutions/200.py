class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res=0
        def dfs(i, j):
            if i > m-1 or i < 0 or j > n-1 or j < 0:
                return

            if grid[i][j] != '1':
                return

            grid[i][j]='#'

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res+=1
        
        return res