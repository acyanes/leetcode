class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = oranges = 0
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oranges+=1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        while q:
            x,y,t = q.popleft()
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                xx,yy=dx+x,dy+y
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy]==1:
                    grid[xx][yy]=2
                    q.append((xx,yy,t+1))
                    time=max(time,t+1)
                    oranges-=1           
        return time if oranges == 0 else -1