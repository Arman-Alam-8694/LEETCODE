from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #KIND OF BRUTE FORCE SOLUTION NOT GOOD FOR LOT OF UNIQUE DOMAINS
        #BUT AS THE DOMAINS HERE IS LIMITED TO LOWERCASE A-Z IT'S ONLY O(26) PER MERGE
        #SO THIS WORKS FINE WE COULD HAVE ALSO USED DFS/BFS SIMILAR TO THIS 
        #BUT FOR THIS PROBLEM I WAS GETTING COOL 100% SO I WILL KEEP MY BRUTE FORCE 
        #KIND OF SOLUTION
        
        char_to_slot = {}
        slot_min_char = []
        cur_slot = 0

        for a, b in zip(s1, s2):
            slot_a = char_to_slot.get(a)
            slot_b = char_to_slot.get(b)

            if slot_a is not None and slot_b is not None:
                if slot_a != slot_b:
                    # Merge slot_b into slot_a (lower index preferred)
                    if slot_min_char[slot_b] < slot_min_char[slot_a]:
                        slot_a, slot_b = slot_b, slot_a
                    for ch in char_to_slot:
                        if char_to_slot[ch] == slot_b:
                            char_to_slot[ch] = slot_a
                    slot_min_char[slot_a] = min(slot_min_char[slot_a], slot_min_char[slot_b])
            elif slot_a is not None:
                char_to_slot[b] = slot_a
                slot_min_char[slot_a] = min(slot_min_char[slot_a], a, b)
            elif slot_b is not None:
                char_to_slot[a] = slot_b
                slot_min_char[slot_b] = min(slot_min_char[slot_b], a, b)
            else:
                char_to_slot[a] = char_to_slot[b] = cur_slot
                slot_min_char.append(min(a, b))
                cur_slot += 1

        result = []
        for ch in baseStr:
            if ch in char_to_slot:
                result.append(slot_min_char[char_to_slot[ch]])
            else:
                result.append(ch)
        return "".join(result)
        
        #BUT USING UNION-FIND IS MOST IMPORTANT FOR LARGER DOMAINS SO WE DO THIS 

        # parent={}
        #initialize each element parent to itself
        # for i in set(baseStr+s1+s2):
        #     parent[i]=i
        #suppose we have a and it's parent is not a then we have find the parent of 
        #it's parent until the parent are same that means here by lexicographically smallest
        #one will the parent to itself and also forming the chains and we use recursion 
        #to change the parents of all the bigger one to this smaller one using find recursion
        # def find(x):
        #     if parent[x]!=x:
        #         parent[x]=find(parent[x])
        #     return parent[x]

        #making union function to do this job of mergin two disjoint sets into one by 
        #priotizing the smaller root of both the set and assiginng it to the bigger one
        # def union(a,b):
        #     rootA=find(a)
        #     rootB=find(b)
        #     if rootA!=rootB:
        #         if rootB<rootA:
        #             parent[rootA]=rootB
        #         else:
        #             parent[rootB]=rootA

        # for i,j in zip(s1,s2):
        #     union(i,j)

        # result=[]
        # for i in baseStr:
        #     result.append(find(i))
        # return "".join(result)
