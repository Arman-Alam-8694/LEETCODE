class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        right=[]
        n=len(height)
        for i in range(n):
            if left and left[-1]>height[i]:
                left.append(left[-1])
            else:
                left.append(height[i])
        
        for i in range(n-1,-1,-1):
            if right and right[-1]>height[i]:
                right.append(right[-1])
            else:
                right.append(height[i])
        right=right[::-1]
        answer=0
        for i in range(n):
            minn=min(left[i],right[i])
            if height[i]<minn:
                answer+=(minn-height[i])
        return answer

        