class Solution {
    public int triangularSum(int[] nums) {
        while(nums.length!=1){
            int[] n=new int[nums.length-1];
            for(int i=0;i<nums.length-1;i++){
                int elem=(nums[i]+nums[i+1])%10;
                n[i]=elem;

            }
            nums=n;

        }
        return nums[0];
        
    }
}