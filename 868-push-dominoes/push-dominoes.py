class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result=""
        dots=0
        prev=None
        for i in dominoes:
            # if i=="L":
            #     if dots!=0 and prev=="R":
            #         result+="R"*(dots//2)
            #         if dots&1:
            #             result+="."
            #         result+="L"*(dots//2)
            #         dots=0
            #     elif prev==None or prev=="L":
            #         result+="L"*dots
            #         dots=0
            #     prev="L"
            #     result+=i
            # elif i==".":
            #     dots+=1
            # elif i=="R":
            #     if dots>0 and (prev==None or prev=="L"):
            #         result+="."*dots
            #         dots=0
            #     elif prev=="R" and dots>0:
            #         result+="R"*dots
            #         dots=0
                
            #     prev="R"
            #     result+=i
            if i==".":
                dots+=1
            else:
                if prev=="R" and i=="R":
                    result+="R"*(dots+1)
                elif prev=="R" and i=="L":
                    result+="R"*(dots//2) 
                    if dots&1:
                        result+="." 
                    result+="L"*(dots//2+1)
                elif (prev=="L" or prev==None) and i=="L":
                    result+="L"*(dots+1)
                elif prev=="L" and i=="R":
                    result+="."*dots
                    result+="R"
                elif prev==None:
                    if i=="R":
                        result+="."*dots
                        result+="R"
                    elif i=="L":
                        result+="L"*(dots+1)
                dots=0
                prev=i


                

        if dots>0:
            if prev=="R":
                result+="R"*dots
            else:
                result+="."*dots

        return result

            
        