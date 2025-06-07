class Solution:
    def clearStars(self, s: str) -> str:
        # abcdefghijklmnopqrstuvwxyz
        char_idx=[[] for _ in range(27)]
        # print(char_idx)
        # rem=ord("a")
        n=len(s)
        smallest=28
        skip=set()
        for i in range(n):
            if s[i]=="*":
                skip.add(i)
                # print(f"before smallest{smalles/t},char_idx {char_idx[smallest]}")
                t=char_idx[smallest].pop()
                skip.add(t)
                # print(f"after pop smallest{smallest},char_idx {char_idx[smallest]}")
                if len(char_idx[smallest])==0:
                    temp=smallest
                    smallest=26
                    for j in range(temp,26):
                        if len(char_idx[j])>=1:
                            smallest=j
                            break
                # print(f"change smallest{smallest},char_idx {char_idx[smallest]}")
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
        