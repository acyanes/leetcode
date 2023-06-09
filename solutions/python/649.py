class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)

        for i, char in enumerate(senate):
            if char == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            n+=1
            if r[0] < d[0]:
                r.append(n)
            else:
                d.append(n)
            r.popleft()
            d.popleft()
        return 'Radiant' if len(d) == 0 else 'Dire'
        

        