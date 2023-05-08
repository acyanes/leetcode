class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index):
            if index >= len(nums):
                return 0 
            
            if index in cache:
                return cache[index]
            
            take=nums[index]+dp(index+2)
            skip=dp(index+1)

            cache[index]=max(take,skip)
            return cache[index]
        cache={}  
        return dp(0)