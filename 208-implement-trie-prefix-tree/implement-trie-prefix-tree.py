class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False


class Trie:

    def __init__(self):
        self.root=TrieNode()
      
 
        

    def insert(self, word: str) -> None:
        curr=self.root
        temp=0
        for a in word:
            if a not in curr.children:
                curr.children[a]=TrieNode()
            curr=curr.children[a]
        curr.endofword=True
      
    
        

    def search(self, word: str) -> bool:
        curr=self.root
        for b in word:
            if b not  in curr.children:
                return False
            curr=curr.children[b]
        return curr.endofword
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for b in prefix:
            if b not  in curr.children:
                return False
            curr=curr.children[b]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)