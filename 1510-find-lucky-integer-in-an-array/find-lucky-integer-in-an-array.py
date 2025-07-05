# class Solution {
#     public int findLucky(int[] arr) {
#         Map<Integer,Integer> map=new HashMap<>();
#         for(int i=0;i<arr.length;i++){
#             map.put(arr[i],map.getOrDefault(arr[i],0)+1);
#         }
        
#         Set<Map.Entry<Integer,Integer>> map_entry=map.entrySet();
#         int result=-1;
#         // Set<Integer> map_keys=map.keySet();
#         for(Map.Entry<Integer,Integer> i:map_entry){
#             if (i.getValue().equals(i.getKey())){
#                 result=Math.max(result,i.getKey());
#             }
#         }
#         return result;
#     }
# }


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mapp=Counter(arr)
        result=-1
        for i,j in mapp.items():
            if i==j:
                result=max(result,i)
        return result

        