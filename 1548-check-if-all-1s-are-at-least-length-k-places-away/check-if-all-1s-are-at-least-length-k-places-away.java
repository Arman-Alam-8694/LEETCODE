class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int prev=-1;
        for(int cur=0;cur<nums.length;cur++){
            if(nums[cur]==1){
                if (prev!=-1 & !((cur-prev-1)>=k)){
                    return false;
                }else{
                    prev=cur;
                }
            }

        }
        return true;
        
    }
}