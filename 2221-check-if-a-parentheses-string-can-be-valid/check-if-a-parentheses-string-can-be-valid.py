class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        left_look=None
        n=len(s)
        if n&1:
            return False
        stack=[]
        visited=set()
      
        for i in range(n):
           
            if s[i]==")" and locked[i]=="1":
                visited.add(i)
                if not stack:
                    if i-1>=0 and (s[i-1]=="(" or locked[i-1]=="0"):
                        if i-2 not in visited:
                            stack.append(i-2)
                        continue
                    else:
                        print(i,stack)
                        return False
                elif i-1>=0 and (s[i-1]=="(" or locked[i-1]=="0"):
                    if i-2 not in visited:
                        stack.append(i-2)
                    continue
                else:
                    idx=stack.pop()
                    if idx>=0 and (s[idx]=="(" or locked[idx]=="0"):
                        if idx-1 not in visited:
                            stack.append(idx-1)
                        continue
                    else:
                        print(i,stack)
                        return False

       
        sr=s[::-1]
       
        lockedr=locked[::-1]
        stack=[]
        visited=set()
        for i in range(n):
            if sr[i]=="(" and lockedr[i]=="1":
                visited.add(i)
                if not stack:
                    if i-1>=0 and (sr[i-1]==")" or lockedr[i-1]=="0"):
                        if i-2 not in visited:
                            stack.append(i-2)
                        continue
                    else:
                        print(i,stack)
                        return False
                elif i-1>=0 and (sr[i-1]==")" or lockedr[i-1]=="0"):
                    if i-2 not in visited:
                        stack.append(i-2)
                    continue
                else:
                    idx=stack.pop()
                    if idx>=0 and (sr[idx]==")" or lockedr[idx]=="0"):
                        if idx-1 not in visited:
                            stack.append(idx-1)
                        continue
                    else:
                        return False
            
        return True

        


