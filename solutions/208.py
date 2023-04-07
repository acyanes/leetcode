class Trie:
    def __init__(self):
        self.d = defaultdict(dict)
        

    def insert(self, word: str) -> None:
        d = self.d
        for char in word:
            if not char in d:
                d[char]={}
            d = d[char]
        d['$']=None


    def search(self, word: str) -> bool:
        d = self.d
        for char in word:
            if char in d:
                d = d[char]
            else:
                return False
        if '$' in d:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)