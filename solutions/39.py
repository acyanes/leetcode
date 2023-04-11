class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, path):
            if index >= len(candidates) or sum(path) > target:
                return
            if sum(path) == target:
                res.append(path)
                return 

            take = backtrack(index, path+[candidates[index]])
            skip = backtrack(index+1, path)

        backtrack(0, [])
        return res