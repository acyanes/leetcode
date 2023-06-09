class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
                
        backtrack(0,[])   
        return res