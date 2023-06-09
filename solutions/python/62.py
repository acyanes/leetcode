class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(i,j):
            if i >= m or j >= n: 
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = dp(i+1,j) + dp(i,j+1)
            return cache[(i,j)]

        cache={}
        return dp(0,0)
