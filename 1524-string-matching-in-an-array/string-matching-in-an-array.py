# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         result=[]
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if words[i] in words[j] and i!=j:
#                     result.append(words[i])
#                     break
#         return result

# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         a = " ".join(words)
#         return [w for w in words if a.count(w)>1]


        
class Solution:
    class TrieNode:
        def __init__(self):
            self.children={}
            self.count=0


    class Trie:
        def __init__(self):
            self.root=Solution.TrieNode()

        def insert(self, word: str) -> None:
            curr=self.root
            temp=0
            for a in word:
                if a not in curr.children:
                    curr.children[a]=Solution.TrieNode()
                curr=curr.children[a]
                curr.count+=1

        def find(self,word):
            curr=self.root
            for c in word:
                curr=curr.children[c]
            return curr.count>1

       

    def stringMatching(self, words: List[str]) -> List[str]:
        t=self.Trie()
        result=[]
        for w in words:
            for i in range(len(w)):
                t.insert(w[i:])
        for w in words:
            if t.find(w):
                result.append(w)
        return result
        

















   