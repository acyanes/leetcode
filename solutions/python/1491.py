class Solution:
    def average(self, salary: List[int]) -> float:
        s = 0
        mn = math.inf
        mx = -math.inf

        for i in range(len(salary)):
            s+=salary[i]
            mn=min(mn, salary[i])
            mx=max(mx,salary[i])
        
        return (s-mn-mx)/(len(salary)-2)

        
