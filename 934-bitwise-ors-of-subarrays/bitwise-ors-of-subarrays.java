// class Solution:
//     def subarrayBitwiseORs(self, arr: List[int]) -> int:
//         res = set()      # all ORs seen so far
//         cur = set()      # ORs of subarrays ending at previous index
//         for x in arr:
//             # new ORs ending at this element:
      
//             nxt = {x} | {x | y for y in cur}
         
//             res |= nxt
//             cur = nxt

//         return len(res)


        


class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> res=new HashSet<>();
        Set<Integer> curr=new HashSet<>();

        for(Integer i:arr){
            Set<Integer> next=new HashSet<>();
            next.add(i);
            for(Integer j:curr){
                next.add(i|j);
            }
            res.addAll(next);
            curr=next;
        }
        return res.size();

        
    }
}