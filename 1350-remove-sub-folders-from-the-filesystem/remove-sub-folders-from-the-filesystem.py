class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        new_folder=set(folder)
        answer=[]
        for fol in folder:
            prefix=list(fol)
            found=False
            while True:
                while prefix and prefix[-1]!="/":
                    prefix.pop()
                if not prefix:
                    break
                prefix.pop()
                new="".join(prefix)
                
                if new in new_folder:
                    found=True
                    break
            if not found:
                answer.append(fol)
        return answer
            
            
            
        