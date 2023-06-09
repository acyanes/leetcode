class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        n = len(accounts)

        def dfs(email, li):
            if not email in seen:
                seen.add(email)
                for neigh in d[email]:
                    for index, addresses in enumerate(accounts[neigh], start=1):
                        if addresses not in li:
                            li.append(addresses)
                        dfs(addresses, li)

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                d[email].append(i)
        
        res, seen = [], set()
        for i in range(n):
            temp = [] # name
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if not email in seen:
                    dfs(email, temp)
                    temp[1:]=sorted(temp[1:])
                    res.append(temp)
        return res