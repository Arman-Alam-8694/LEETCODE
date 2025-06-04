class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        max_string=""
        def get_rank(a):
            return ord(a)-ord("a")
        n=len(word)
        max_contain=n-((numFriends)-1)
        max_char=max(word)
        max_indices=[]
        for i in range(n):
            if word[i]==max_char:
                max_indices.append(i)


        for i in max_indices:
            max_string=max(word[i:i+max_contain],max_string)

        return max_string

        #SAME TC BUT FASTER BECAUSE OF INBUILT FUNCTION IN C LANGUAGE
        # if numFriends == 1:
        #     return word
        # n = len(word) - numFriends + 1
        # return max( word[i:i+n] for i in range(len(word)) )

        