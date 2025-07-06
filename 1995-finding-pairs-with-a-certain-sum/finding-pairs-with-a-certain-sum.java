class FindSumPairs {

    int[] nums1,nums2;
    Map<Integer,Integer> map1=new TreeMap<>();
    Map<Integer,Integer> map2=new HashMap<>();
    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1=nums1;
        this.nums2=nums2;
        for(int i=0;i<this.nums1.length;i++){
            this.map1.put(this.nums1[i],this.map1.getOrDefault(this.nums1[i],0)+1);
        }
        for(int i=0;i<this.nums2.length;i++){
            this.map2.put(this.nums2[i],this.map2.getOrDefault(this.nums2[i],0)+1);

        }

        
    }
    
    public void add(int index, int val) {
        this.map2.put(this.nums2[index],this.map2.get(this.nums2[index])-1);
        if(this.map2.get(this.nums2[index])==0){
            this.map2.remove(this.nums2[index]);
        }
        this.nums2[index]+=val;
        this.map2.put(this.nums2[index],this.map2.getOrDefault(this.nums2[index],0)+1);
        
    }
    
    public int count(int tot) {
        int result=0;
        Set<Integer> set=this.map1.keySet();
        for(Integer e:set){
            if(e>tot){
                break;
            }
            Integer target=tot-e;
            if(e<=tot && this.map2.containsKey(target)){
                result+=this.map2.get(target)*this.map1.get(e);
            }
          
            
        }
        return result;

        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */