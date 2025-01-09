class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0

class PrefixTree:
    def __init__(self):
        self.root=TrieNode()
    def add(self,w):
        curr=self.root
        for a in w:
            if a not in curr.children:
                curr.children[a]=TrieNode()
            curr=curr.children[a]
            curr.count+=1
    def find(self,pref):
        curr=self.root
        for b in pref:
            if b not  in curr.children:
                return 0
            curr=curr.children[b]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        p=PrefixTree()
        for w in words:
            p.add(w)
        return p.find(pref)