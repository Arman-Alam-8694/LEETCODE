class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        size=len(searchWord)
        for idx,word in enumerate(words):
            if word.startswith(searchWord):
                return idx+1
        return -1
        