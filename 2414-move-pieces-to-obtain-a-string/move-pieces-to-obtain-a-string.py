class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left=0
        right=0
        for i in range(len(start)):
            if target[i]=="L":
                left+=1
            if start[i]=="L":
                if left==0 or right!=0:
                    return False
                else:
                    left-=1
            if start[i]=="R":
                right+=1
              
            if target[i]=="R":
                if right==0 or left!=0:
                    return False
                else:
                    right-=1
        if left or right:
            return False
        return True
            