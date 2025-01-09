class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0

class PrefixTree:
    def __init__(self):
        self.root=TrieNode()
    def add(self,w,n):
        curr=self.root
        temp=0
        for a in w:
            if temp==n:
                break
            if a not in curr.children:
                curr.children[a]=TrieNode()
            curr=curr.children[a]
            curr.count+=1
            temp+=1
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
        n=len(pref)
        for w in words:
            if len(w)>=len(pref):
                p.add(w,n)
        return p.find(pref)