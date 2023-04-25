class Solution:
    def longestPalindrome(self, s: str) -> str:
        def dp(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= j:
                return True

            if s[i] != s[j]:
                return False
            
            cache[(i,j)] = dp(i+1, j-1)
            return cache[(i,j)] 

        if len(s) < 2: return s
        cache = {}
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp(i,j):
                    if len(res) < j-i+1:
                        res = s[i:j+1]
        return res