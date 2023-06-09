class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        seen=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i,j,0))

        while q:
            x,y,d=q.popleft()
            if grid[x][y]=='#':
                return d
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                newx,newy=dx+x,dy+y
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != 'X':
                    if (newx,newy) not in seen:
                        seen.add((newx,newy))
                        q.append((newx,newy,d+1))
        return -1