class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        same=False
        result=0
        for k,v in count.items():
            rev=k[::-1]
            if v==0:
                continue
            if rev in count:
                if rev==k:
                    result+=4*(count[rev]//2)
                    if count[rev]&1:
                        same=True
                    count[rev]=0
                else:
                    result+=4*(min(count[k],count[rev]))
                    count[k]=0
                    count[rev]=0
        return result if not same else result+2
