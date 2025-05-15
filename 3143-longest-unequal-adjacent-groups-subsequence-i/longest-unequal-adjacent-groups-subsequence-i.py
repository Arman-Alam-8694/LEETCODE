class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        largest=[]
        prev=groups[0]
        largest.append(words[0])
        for i in range(1,len(words)):
            if groups[i]!=prev:
                largest.append(words[i])
                prev=groups[i]
        return largest

        