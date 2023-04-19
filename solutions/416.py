class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(target, index):
            if target < 0:
                return False
            if target == 0:
                return True
            if index>=len(nums):
                return False
            if (target, index) in cache:
                return cache[(target,index)]
            take_skip = dfs(target-nums[index],index+1) or dfs(target, index+1)
            cache[(target,index)]=take_skip
            return cache[(target,index)]

        s = sum(nums)
        cache = {}
        if s % 2 == 1:
            return False
        return dfs(s//2,0)
        
        
        
# using lru_cache decorator
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(target, index):
            if target < 0:
                return False
            if target == 0:
                return True
            if index>=len(nums):
                return False
            
            return dfs(target-nums[index], index+1) or dfs(target, index+1)

        s = sum(nums)
        if s % 2 == 1:
            return False
        return dfs(s//2,0)
        
        
        