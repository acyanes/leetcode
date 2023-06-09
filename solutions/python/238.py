# o(n) space solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = [0] * n
        right = [0] * n

        left[0]=1
        product=1
        for i in range(1,n):
            product *= nums[i-1]
            left[i] = product

        right[n-1]=1
        product=1
        for i in range(n-2,-1,-1):
            product*=nums[i+1]
            right[i]=product
        
        for i in range(n):
            res[i]=left[i]*right[i]

        

        return res
    
# O(1) solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        curr = 1
        for i in range(n):
            res[i] *= curr
            curr *= nums[i]
        
        curr = 1
        for i in range(n-1,-1,-1):
            res[i]*=curr
            curr*=nums[i]
       
        return res