class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for i in letters:
        #     if ord(i)>ord(target):
        #         return i
        # return letters[0]
        left=0
        right=len(letters)-1
        while left<=right:
            mid=(left+right)//2
            curr=letters[mid]
            if ord(curr)>ord(target):
                right=mid-1
            else:
                left=mid+1
        return letters[left] if left!=len(letters) else letters[0]

        