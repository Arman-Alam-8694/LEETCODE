from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dq=deque([])
        n=len(digits)
        carry=0
        for i in range(n-1,-1,-1):
            if i==n-1 or (dq and carry):
                curr=digits[i]+1
                
                if curr>=10:
                    carry=curr//10
                    curr=curr%10
                    # print(curr,carry)
                else:
                    carry=0

                dq.appendleft(curr)
            else:
                dq.appendleft(digits[i])

        if carry:
            dq.appendleft(1)
        # print(dq,carry)
        return list(dq)

