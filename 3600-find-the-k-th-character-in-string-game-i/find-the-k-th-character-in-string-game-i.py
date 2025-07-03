class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            temp=""
            for i in word:
                new=(ord(i)+1)%(ord("z")+1)
                temp+=chr(new)
            word=word+temp
            print(word)
        return word[k-1]
        