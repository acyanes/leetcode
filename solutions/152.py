class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = maxx = nums[0]
        res = maxx

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, curr*maxx, curr*minn)
            minn = min(curr, curr*minn, curr*maxx)
            maxx=temp
            res = max(res,maxx)

        return res