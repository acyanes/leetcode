class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        res=0
        j=n-1
        for i in range(m):
            res+=mat[i][i]
            if j!=i:
                res+=mat[i][j]
            j-=1
        return res