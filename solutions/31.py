class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(index):
            jj = len(nums)-1
            while index < jj:
                nums[index], nums[jj] = nums[jj], nums[index]
                index+=1
                jj-=1
        
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # no greater element to be made
        if i == -1:
            reverse(0)
            return
        
        # find first greatest element
        j=len(nums)-1
        while i < j and nums[i]>=nums[j]:
            j-=1
        
        #swap here
        nums[i],nums[j]=nums[j],nums[i]

        #reverse everything from i+1
        reverse(i+1)


        """
        Do not return anything, modify nums in-place instead.
        """