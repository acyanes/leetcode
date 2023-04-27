class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,wordIndex,seen):
            if wordIndex==len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if (i,j) in seen:
                return False

            if board[i][j] == word[wordIndex]:
                wordIndex+=1
                seen.add((i,j))
                
                a=dfs(i-1,j,wordIndex,seen)
                b=dfs(i+1,j,wordIndex,seen)
                c=dfs(i,j-1,wordIndex,seen)
                d=dfs(i,j+1,wordIndex,seen)

                seen.remove((i,j))
                return a or b or c or d

        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0,set()):
                        return True
        return False