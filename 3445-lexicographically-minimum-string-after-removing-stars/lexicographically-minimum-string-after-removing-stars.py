class Solution:
    def clearStars(self, s: str) -> str:
        # abcdefghijklmnopqrstuvwxyz
        char_idx=[[] for _ in range(27)]
        # print(char_idx)
        rem=ord("a")
        n=len(s)
        smallest=28
        skip=set()
        for i in range(n):
            if s[i]=="*":
                # print(char_idx)
                # print(f"curr {i} smallest{smallest} char_idx-{char_idx[smallest]}")
                skip.add(i)
                for j in range(smallest,26):
                    if len(char_idx[j])>=1:
                        smallest=j
                        break
                t=char_idx[smallest].pop()
                skip.add(t)
                    
            else:
                new=ord(s[i])-ord("a")
                if new<=smallest:
                    smallest=new
                char_idx[new].append(i)
        # print(skip)
        result=[]
        for i in range(n):
            if i not in skip:
                result.append(s[i])
        return "".join(result)
        