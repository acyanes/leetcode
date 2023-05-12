class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def dp(i,j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if nums1[i]==nums2[j]:
                return 1 + dp(i+1,j+1)
            cache[(i,j)] = max(dp(i+1,j), dp(i,j+1))
            return cache[(i,j)]
        cache={}
        return dp(0,0)