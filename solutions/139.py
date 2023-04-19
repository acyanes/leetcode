class TrieNode:
    def __init__(self, character):
        self.character = character
        self.nodes = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.t = TrieNode(None)
        self.cache = {}

    # time: O(N) where N is len(word)
    def add(self, word):
        t = self.t
        for char in word:
            if not char in t.nodes:
                t.nodes[char] = TrieNode(char)
            t = t.nodes[char]
        t.isWord=True
                
    # time: O(K) where K is len(s)
    def contains(self, word):
        t = self.t
        cache = self.cache
        if word in cache:
            return cache[word]

        for i, char in enumerate(word):
            if not char in t.nodes:
                cache[word]=False
                return False  

            if t.nodes[char].isWord:
                newWord = word[i+1:]
                if self.contains(newWord):
                    cache[newWord]=True
                    return True
            t = t.nodes[char]
        cache[word]=t.isWord
        return cache[word]
        
            
class Solution:
    # time: O(N*K)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        return trie.contains(s)
