class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        def backtrack(i,path):
            if len(path)==len(digits):
                res.append(''.join(path[:]))
                return
            
            characters = m[digits[i]]
            for index in range(len(characters)):
                path.append(characters[index])
                backtrack(i+1,path)
                path.pop()
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]
        backtrack(0,[])
        return res