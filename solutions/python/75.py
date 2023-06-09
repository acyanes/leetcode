# merge sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(arr):
            if len(arr)>1:
                mid = len(arr)//2
                left_half = arr[:mid]
                right_half = arr[mid:]
                merge(left_half)
                merge(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] <= right_half[j]:
                        arr[k]=left_half[i]
                        i+=1
                    else:
                        arr[k]=right_half[j]
                        j+=1
                    k+=1
                
                while i < len(left_half):
                    arr[k]=left_half[i]
                    k+=1
                    i+=1

                while j < len(right_half):
                    arr[k]=right_half[j]
                    k+=1
                    j+=1
        merge(nums)

# bubble sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]