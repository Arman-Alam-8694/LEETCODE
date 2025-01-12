class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        if n&1:
            return False
        stack=[]
        visited=set()
        for i in range(n):
            if s[i]==")" and locked[i]=="1":
                visited.add(i)
                if i-1>=0 and (s[i-1]=="(" or locked[i-1]=="0"):
                    if i-2 not in visited:
                        stack.append(i-2)
                    continue
                elif stack:
                    idx=stack.pop()
                    if idx>=0 and (s[idx]=="(" or locked[idx]=="0"):
                        if idx-1 not in visited:
                            stack.append(idx-1)
                        continue
                    else:
                        return False
                else:
                    return False
        
        stack=[]
        visited=set()
        for i in range(n-1,-1,-1):
            if s[i]=="(" and locked[i]=="1":
                visited.add(i)
                if i+1<n and (s[i+1]==")" or locked[i+1]=="0"):
                    if i+2 not in visited:
                        stack.append(i+2)
                    continue
                elif stack:

                    idx=stack.pop()
                    if idx<n and (s[idx]==")" or locked[idx]=="0"):
                        if idx+1 not in visited:
                            stack.append(idx+1)
                        continue
                    else:
                        return False
                else:
                    return False
            
        return True

        


