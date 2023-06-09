class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, path):
            if i > len(nums):
                return
            res.append(path[:])
            for index in range(i, len(nums)):
                path.append(nums[index])
                backtrack(index+1, path)
                path.pop()
    
        res = []
        backtrack(0, [])
        return res