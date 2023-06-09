class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            sort = sorted(''.join(s.split()))
            mp[''.join(sort)].append(s)
        
        res = []
        for k,v in mp.items():
            res.append(v)
        return res