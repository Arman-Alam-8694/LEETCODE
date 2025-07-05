class Solution {
    public int findLucky(int[] arr) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<arr.length;i++){
            map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        }
        
        // List<Map.Entry<Integer>>map_entry=map.entrySet()
        int result=-1;
        Set<Integer> map_keys=map.keySet();
        for(Integer i:map_keys){
            if (map.get(i)==i){
                result=Math.max(result,i);
            }
        }
        return result;
    }
}
